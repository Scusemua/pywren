#
# Copyright 2018 PyWren Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function
import os
import base64
import shutil
import json
import sys
import time
import boto3
from botocore.vendored.requests.packages.urllib3.exceptions import ReadTimeoutError

import io
from six.moves import cPickle as pickle
from tblib import pickling_support

pickling_support.install()
S3_GET_BACKOFF = 0.2
S3_GET_MAX_TRIES = 5


def b64str_to_bytes(str_data):
    str_ascii = str_data.encode('ascii')
    byte_data = base64.b64decode(str_ascii)
    return byte_data

# initial output file in case job fails
output_dict = {'result' : None,
               'success' : False}

pickled_output = pickle.dumps(output_dict)
jobrunner_config_filename = sys.argv[1]

jobrunner_config = json.load(open(jobrunner_config_filename, 'r'))


# FIXME someday switch to storage handler
# download the func data into memory
s3_client = boto3.client("s3")

func_bucket = jobrunner_config['func_bucket']
func_key = jobrunner_config['func_key']

data_bucket = jobrunner_config['data_bucket']
data_key = jobrunner_config['data_key']
data_byte_range = jobrunner_config['data_byte_range']

output_bucket = jobrunner_config['output_bucket']
output_key = jobrunner_config['output_key']

## Jobrunner stats are fieldname float
jobrunner_stats_filename = jobrunner_config['stats_filename']
# open the stats filename
stats_fid = open(jobrunner_stats_filename, 'w')

def write_stat(stat, val):
    stats_fid.write("{} {:f}\n".format(stat, val))
    stats_fid.flush()

def get_pickled_object_with_backoff(s3_client, bucket, key, max_tries=S3_GET_MAX_TRIES, 
                                    backoff=S3_GET_BACKOFF, **extra_get_args):
    """
    Get a pickled S3 object and unpickle it in a streaming fashion. 

    There is substantial retry and error-handling logic here to deal
    with contested objects and S3 errors whcih crop up from time to time

    Will either return correct value or raise exception
    """
    num_tries = 1
    num_timeouts = 0
    time_start = time.time()
    while (num_tries <= max_tries):
        try:
            func_obj_stream = s3_client.get_object(Bucket=bucket, Key=key, **extra_get_args)
            streaming_body = func_obj_stream['Body']
            # THIS IS A BAD IDEA: directly accessing the raw stream is NOT SUPPORTED
            # but I could find no other way to stream this in.
            buffered_io = io.BufferedReader(streaming_body._raw_stream)
            obj = pickle.load(buffered_io)
            break
        except (ReadTimeoutError, pickle.UnpicklingError):
            time.sleep(backoff)
            backoff *= 2
            num_tries += 1
            num_timeouts += 1
    if num_tries > max_tries:
        raise Exception("get_object_with_backoff exceeded max_tries {}".format(num_tries))
    time_end = time.time()
    total_time = time_end - time_start


    return obj, {'num_tries' : num_tries, 
                 'num_timeouts' : num_timeouts, 
                 'total_time' : total_time}


try:
    func_download_time_t1 = time.time()

    loaded_func_all, func_meta = get_pickled_object_with_backoff(s3_client,
                                                                 bucket=func_bucket, key=func_key)
    for k, v in func_meta.items():

        write_stat("func_{}".format(k), v)

    # load_func_bytes = func_obj_stream['Body'].read()
    # func_download_time_t2 = time.time()
    # write_stat('func_download_time',
    #            func_download_time_t2-func_download_time_t1)
    # write_stat('func_bytes', len(load_func_bytes))

    # loaded_func_all = pickle.loads(load_func_bytes)

    # save modules, before we unpickle actual function
    PYTHON_MODULE_PATH = jobrunner_config['python_module_path']

    shutil.rmtree(PYTHON_MODULE_PATH, True) # delete old modules
    os.mkdir(PYTHON_MODULE_PATH)
    sys.path.append(PYTHON_MODULE_PATH)

    for m_filename, m_data in loaded_func_all['module_data'].items():
        m_path = os.path.dirname(m_filename)

        if len(m_path) > 0 and m_path[0] == "/":
            m_path = m_path[1:]
        to_make = os.path.join(PYTHON_MODULE_PATH, m_path)
        try:
            os.makedirs(to_make)
        except OSError as e:
            if e.errno == 17:
                pass
            else:
                raise e
        full_filename = os.path.join(to_make, os.path.basename(m_filename))
        #print "creating", full_filename
        with open(full_filename, 'wb') as fid:
            fid.write(b64str_to_bytes(m_data))

    # logger.info("Finished wrting {} module files".format(len(d['module_data'])))
    # logger.debug(subprocess.check_output("find {}".format(PYTHON_MODULE_PATH), shell=True))
    # logger.debug(subprocess.check_output("find {}".format(os.getcwd()), shell=True))


    # now unpickle function; it will expect modules to be there
    loaded_func = pickle.loads(loaded_func_all['func'])

    extra_get_args = {}
    if data_byte_range is not None:
        range_str = 'bytes={}-{}'.format(*data_byte_range)
        extra_get_args['Range'] = range_str

    data_download_time_t1 = time.time()
    loaded_data, data_meta = get_pickled_object_with_backoff(s3_client, bucket=data_bucket,
                                                            key=data_key,
                                                            **extra_get_args)
    for k, v in data_meta.items():
        
        write_stat('data_{}'.format(k), v)

    # # FIXME make this streaming
    # loaded_data = pickle.loads(data_obj_stream['Body'].read())
    # data_download_time_t2 = time.time()
    # write_stat('data_download_time',
    #            data_download_time_t2-data_download_time_t1)

    #print("loaded")
    y = loaded_func(loaded_data)
    #print("success")
    output_dict = {'result' : y,
                   'success' : True,
                   'sys.path' : sys.path}
    pickled_output = pickle.dumps(output_dict)

except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    #traceback.print_tb(exc_traceback)

    # Shockingly often, modules like subprocess don't properly
    # call the base Exception.__init__, which results in them
    # being unpickleable. As a result, we actually wrap this in a try/catch block
    # and more-carefully handle the exceptions if any part of this save / test-reload
    # fails

    try:
        pickled_output = pickle.dumps({'result' : e,
                                       'exc_type' : exc_type,
                                       'exc_value' : exc_value,
                                       'exc_traceback' : exc_traceback,
                                       'sys.path' : sys.path,
                                       'success' : False})

        # this is just to make sure they can be unpickled
        pickle.loads(pickled_output)

    except Exception as pickle_exception:
        pickled_output = pickle.dumps({'result' : str(e),
                                       'exc_type' : str(exc_type),
                                       'exc_value' : str(exc_value),
                                       'exc_traceback' : exc_traceback,
                                       'exc_traceback_str' : str(exc_traceback),
                                       'sys.path' : sys.path,
                                       'pickle_fail' : True,
                                       'pickle_exception' : pickle_exception,
                                       'success' : False})
finally:
    output_upload_timestamp_t1 = time.time()
    s3_client.put_object(Body=pickled_output,
                         Bucket=output_bucket,
                         Key=output_key)
    output_upload_timestamp_t2 = time.time()
    write_stat("output_upload_time",
               output_upload_timestamp_t2 - output_upload_timestamp_t1)
    stats_fid.close()
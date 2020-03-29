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

import botocore
import redis 

from .exceptions import StorageNoSuchKeyError

class RedisBackend(object):
    """
    A wrap-up around S3 boto3 APIs.
    """

    def __init__(self, redis_config):
        self.bucket = redis_config['bucket']
        self.host = redis_config["host"]
        self.port = redis_config["port"]
        self.redis_client = redis.StrictRedis(host=self.host, port=self.port)

    def put_object(self, key, data):
        """
        Put an object in Redis. Override the object if the key already exists.
        :param key: key of the object.
        :param data: data of the object
        :type data: str/bytes
        :return: None
        """
        self.redis_client.set(self.bucket + key, data)

    def get_object(self, key):
        """
        Get object from Redis with a key. Throws StorageNoSuchKeyError if the given key does not exist.
        :param key: key of the object
        :return: Data of the object
        :rtype: str/bytes
        """
        r = self.redis_client.get(self.bucket + key)
        
        if r is None:
            raise StorageNoSuchKeyError(self.bucket + key)
        
    def key_exists(self, key):
        """
        Check if a key exists in Redis.
        :param key: key of the object
        :return: True if key exists, False if not exists
        :rtype: boolean
        """
        return self.redis_client.exists(self.bucket + key)

    def list_keys_with_prefix(self, prefix):
        """
        Return a list of keys for the given prefix.
        :param prefix: Prefix to filter object names.
        :return: List of keys in bucket that match the given prefix.
        :rtype: list of str
        """
        match = self.bucket + str(prefix) + "*"

        key_list = []
        for key in self.redis_client.scan_iter(count=100, match=match):
            key_list.append(key)

        return key_list

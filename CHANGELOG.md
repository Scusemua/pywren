# Change Log


## [v0.4](https://github.com/pywren/pywren/tree/v0.4rc0) (2018-11-05)
[Full Changelog](https://github.com/pywren/pywren/compare/v0.3.0...v0.4rc0)

**Implemented enhancements:**

- Expose SQS queue length from command line [\#215](https://github.com/pywren/pywren/issues/215)
- Create ability to cancel jobs [\#187](https://github.com/pywren/pywren/issues/187)

**Fixed bugs:**

- import ALWAYS wait state into top level module [\#201](https://github.com/pywren/pywren/issues/201)
- standalone non-deterministically drops jobs when \> 50 instances are spun up [\#197](https://github.com/pywren/pywren/issues/197)
- Pickling pytorch model causes error [\#190](https://github.com/pywren/pywren/issues/190)
- Executor won't run from shard if numshards = 1 [\#189](https://github.com/pywren/pywren/issues/189)
- restore \_\_version\_\_ [\#186](https://github.com/pywren/pywren/issues/186)
- lapack/blas calls very slow on multicore machines for stand alone mode [\#137](https://github.com/pywren/pywren/issues/137)

**Closed issues:**

- Python 3.7 runtime [\#267](https://github.com/pywren/pywren/issues/267)
- LocalInvoker only on Linux breaks all CLI  on OSX/\(maybe windows\) [\#291](https://github.com/pywren/pywren/issues/291)
- click 7.0 release changed command line options [\#288](https://github.com/pywren/pywren/issues/288)
- standalone setup improvements [\#284](https://github.com/pywren/pywren/issues/284)
- sklearn usage example [\#280](https://github.com/pywren/pywren/issues/280)
- wrenhandler imports fcntl which is system specific [\#272](https://github.com/pywren/pywren/issues/272)
- WaitTest::test\_all\_complete  fails in standalone mode some times due to botocore timeouts [\#268](https://github.com/pywren/pywren/issues/268)
- pywren setup error: no module named pywren [\#261](https://github.com/pywren/pywren/issues/261)
- Bucket already exists error [\#260](https://github.com/pywren/pywren/issues/260)
- No module named 'pwd' [\#259](https://github.com/pywren/pywren/issues/259)
- pywren-setup: ModuleNotFoundError: No module named 'pwd' [\#257](https://github.com/pywren/pywren/issues/257)
- create\_instance\_profile fails if profile already exists [\#254](https://github.com/pywren/pywren/issues/254)
- eu-west-1 runtime bucket not existing / not public [\#252](https://github.com/pywren/pywren/issues/252)
- Question about map result and wait function [\#250](https://github.com/pywren/pywren/issues/250)
- Pywren and Amazon RDS issue [\#248](https://github.com/pywren/pywren/issues/248)
- Guide needed: How to use' extra\_meta ' parameter in pywren executor? [\#244](https://github.com/pywren/pywren/issues/244)
- pywren not functioning as expected on windows develepment env [\#243](https://github.com/pywren/pywren/issues/243)
- pywren-setup ends with no module named pywren [\#242](https://github.com/pywren/pywren/issues/242)
- Provide profile option  [\#240](https://github.com/pywren/pywren/issues/240)
- Add license headers to all files [\#234](https://github.com/pywren/pywren/issues/234)
- AccessDenied after installation with default settings? [\#232](https://github.com/pywren/pywren/issues/232)
- Multiple Executors on single standalone instance [\#216](https://github.com/pywren/pywren/issues/216)
- half-implemented wrapped stream handler causes runtime untar errors on py2.7 [\#211](https://github.com/pywren/pywren/issues/211)
- remove numpy dependency [\#205](https://github.com/pywren/pywren/issues/205)
- SQS Create queue ignores custom config file [\#204](https://github.com/pywren/pywren/issues/204)
- List keys with prefix assumes at least one entry [\#203](https://github.com/pywren/pywren/issues/203)
- Add download statistics back for func/data/output [\#188](https://github.com/pywren/pywren/issues/188)
- pywren.wait\(\) only works for futures of same job [\#179](https://github.com/pywren/pywren/issues/179)
- Clean up devnotes [\#165](https://github.com/pywren/pywren/issues/165)
- Passing pylint should be a prerequisite for actual travis tests [\#149](https://github.com/pywren/pywren/issues/149)

**Merged pull requests:**

- Release0.4/new runtime buckets [\#293](https://github.com/pywren/pywren/pull/293) ([Vaishaal](https://github.com/Vaishaal))
- fix for non-linux machines [\#292](https://github.com/pywren/pywren/pull/292) ([zehric](https://github.com/zehric))
- fix standalone setup errors [\#289](https://github.com/pywren/pywren/pull/289) ([zehric](https://github.com/zehric))
- fix cli options for click 7.0 [\#287](https://github.com/pywren/pywren/pull/287) ([zehric](https://github.com/zehric))
- added sqs queue size and instance uptimes in cli [\#285](https://github.com/pywren/pywren/pull/285) ([zehric](https://github.com/zehric))
- Fix typo in s3\_backend.py [\#283](https://github.com/pywren/pywren/pull/283) ([rjboczar](https://github.com/rjboczar))
- clean up local invoker [\#282](https://github.com/pywren/pywren/pull/282) ([zehric](https://github.com/zehric))
- refactor wrenhandler to be less os-specific [\#281](https://github.com/pywren/pywren/pull/281) ([zehric](https://github.com/zehric))
- fix for windows path separator issues [\#279](https://github.com/pywren/pywren/pull/279) ([zehric](https://github.com/zehric))
- windows fix for file locking [\#278](https://github.com/pywren/pywren/pull/278) ([zehric](https://github.com/zehric))
- fix wait on multiple callset\_ids [\#277](https://github.com/pywren/pywren/pull/277) ([zehric](https://github.com/zehric))
- windows fix for pwd [\#276](https://github.com/pywren/pywren/pull/276) ([zehric](https://github.com/zehric))
- add exp backoff in jobrunner get\_object so it doesn't fail on start [\#269](https://github.com/pywren/pywren/pull/269) ([Vaishaal](https://github.com/Vaishaal))
- newer versions of pylint became more strict [\#265](https://github.com/pywren/pywren/pull/265) ([Vaishaal](https://github.com/Vaishaal))
- Custom lookup runtime regions [\#255](https://github.com/pywren/pywren/pull/255) ([ericmjonas](https://github.com/ericmjonas))
- do not error if iam role already exists during setup [\#246](https://github.com/pywren/pywren/pull/246) ([Vaishaal](https://github.com/Vaishaal))
- use items\(\) not iteritems\(\) since python3 doesn't have iteritems\(\) [\#245](https://github.com/pywren/pywren/pull/245) ([Vaishaal](https://github.com/Vaishaal))
- License update for serialize module [\#241](https://github.com/pywren/pywren/pull/241) ([ooq](https://github.com/ooq))
- Add license headers. [\#238](https://github.com/pywren/pywren/pull/238) ([ooq](https://github.com/ooq))
- Move jobrunner to dir [\#228](https://github.com/pywren/pywren/pull/228) ([ericmjonas](https://github.com/ericmjonas))
- Standalone multiple executors [\#224](https://github.com/pywren/pywren/pull/224) ([Vaishaal](https://github.com/Vaishaal))
- Process failure properly captured [\#223](https://github.com/pywren/pywren/pull/223) ([ericmjonas](https://github.com/ericmjonas))
- Travis [\#213](https://github.com/pywren/pywren/pull/213) ([apengwin](https://github.com/apengwin))
- move from using wrappedstreamhandler to bytesio and read [\#212](https://github.com/pywren/pywren/pull/212) ([ericmjonas](https://github.com/ericmjonas))
- Fix two simple bugs [\#207](https://github.com/pywren/pywren/pull/207) ([ericmjonas](https://github.com/ericmjonas))
- remove numpy dep [\#206](https://github.com/pywren/pywren/pull/206) ([ericmjonas](https://github.com/ericmjonas))
- Fix issue 199 [\#200](https://github.com/pywren/pywren/pull/200) ([ericmjonas](https://github.com/ericmjonas))
- Standalone bug-fixes [\#198](https://github.com/pywren/pywren/pull/198) ([ericmjonas](https://github.com/ericmjonas))
- Add ability to cancel a job \[WIP\] [\#196](https://github.com/pywren/pywren/pull/196) ([ericmjonas](https://github.com/ericmjonas))
- Created per-handler-type env vars to fix \#137 [\#194](https://github.com/pywren/pywren/pull/194) ([ericmjonas](https://github.com/ericmjonas))
- Fix issue 186 [\#193](https://github.com/pywren/pywren/pull/193) ([ericmjonas](https://github.com/ericmjonas))
- add download stats back in, fixes 188 [\#192](https://github.com/pywren/pywren/pull/192) ([ericmjonas](https://github.com/ericmjonas))
- Upgrade cloudpickle to 0.4.0 [\#191](https://github.com/pywren/pywren/pull/191) ([ericmjonas](https://github.com/ericmjonas))
- Migrate s3io to jobrunner [\#180](https://github.com/pywren/pywren/pull/180) ([ericmjonas](https://github.com/ericmjonas))
- Docs [\#168](https://github.com/pywren/pywren/pull/168) ([apengwin](https://github.com/apengwin))

## [v0.3.0](https://github.com/pywren/pywren/tree/v0.3.0) (2017-09-07)
[Full Changelog](https://github.com/pywren/pywren/compare/v0.2...v0.3.0)

**Fixed bugs:**

- Test Function doesn't parse command-line config [\#166](https://github.com/pywren/pywren/issues/166)

**Closed issues:**

- Error with None result [\#183](https://github.com/pywren/pywren/issues/183)
- Create max list seatbelt [\#176](https://github.com/pywren/pywren/issues/176)
- Make ALL\_COMPLETED, ANY\_COMPLETED, and ALWAYS available without having to specifically import [\#174](https://github.com/pywren/pywren/issues/174)
- Generic Release clean-up [\#171](https://github.com/pywren/pywren/issues/171)
- Change default runtime URLS to be region-specific [\#164](https://github.com/pywren/pywren/issues/164)
- config files manually loaded must be patched with storage config [\#162](https://github.com/pywren/pywren/issues/162)
- Straggler due to list-after-write consistency [\#160](https://github.com/pywren/pywren/issues/160)
- Do not proceed with travis build if pylint fails. [\#157](https://github.com/pywren/pywren/issues/157)
- I can't run test function [\#156](https://github.com/pywren/pywren/issues/156)
- Describe .pywren\_config in "getting started" [\#134](https://github.com/pywren/pywren/issues/134)
- Mapping over an empty list should return an empty list [\#129](https://github.com/pywren/pywren/issues/129)
- Create License File [\#116](https://github.com/pywren/pywren/issues/116)
- Refactor storage APIs [\#108](https://github.com/pywren/pywren/issues/108)
- Too big of runtime [\#105](https://github.com/pywren/pywren/issues/105)
- Update `getting started` webpage on the interactive script [\#103](https://github.com/pywren/pywren/issues/103)
- Have setup.py check for supported python versions [\#101](https://github.com/pywren/pywren/issues/101)
- Support 3.4 runtime \(and others\) [\#95](https://github.com/pywren/pywren/issues/95)
- Migrate travis script to using sec-since-epoch as GUID [\#91](https://github.com/pywren/pywren/issues/91)
- Consider using boto3 s3 transfer interface [\#23](https://github.com/pywren/pywren/issues/23)
- ImportError: No module named 'wren' [\#19](https://github.com/pywren/pywren/issues/19)

**Merged pull requests:**

- \[Issue\#183\] removing none result check [\#184](https://github.com/pywren/pywren/pull/184) ([ooq](https://github.com/ooq))
- Fix issue 91 [\#182](https://github.com/pywren/pywren/pull/182) ([ericmjonas](https://github.com/ericmjonas))
- Release 0.3 [\#178](https://github.com/pywren/pywren/pull/178) ([ericmjonas](https://github.com/ericmjonas))
- New max-limit seatbelt [\#177](https://github.com/pywren/pywren/pull/177) ([ericmjonas](https://github.com/ericmjonas))
- Fix setup py version [\#173](https://github.com/pywren/pywren/pull/173) ([ericmjonas](https://github.com/ericmjonas))
- Lambda toobig seatbelts [\#172](https://github.com/pywren/pywren/pull/172) ([ericmjonas](https://github.com/ericmjonas))
- Issue\#160 Straggler due to list-after-write consistency [\#170](https://github.com/pywren/pywren/pull/170) ([ooq](https://github.com/ooq))
- Switch to region specific runtimes [\#169](https://github.com/pywren/pywren/pull/169) ([ericmjonas](https://github.com/ericmjonas))
- Fix patching of storage handler config, then fix commandline [\#167](https://github.com/pywren/pywren/pull/167) ([ericmjonas](https://github.com/ericmjonas))
- change docstring [\#147](https://github.com/pywren/pywren/pull/147) ([apengwin](https://github.com/apengwin))
- Enable Pylint checks for PyWren [\#144](https://github.com/pywren/pywren/pull/144) ([shivaram](https://github.com/shivaram))
- Pylint cleanup [\#143](https://github.com/pywren/pywren/pull/143) ([shivaram](https://github.com/shivaram))
- Remove cloudpickle dependency and use local cloudpickle. [\#142](https://github.com/pywren/pywren/pull/142) ([ooq](https://github.com/ooq))
- add exclude modules argument to map [\#140](https://github.com/pywren/pywren/pull/140) ([Vaishaal](https://github.com/Vaishaal))
- Handle empty input list in map [\#133](https://github.com/pywren/pywren/pull/133) ([shivaram](https://github.com/shivaram))
- Add Apache v2 License [\#132](https://github.com/pywren/pywren/pull/132) ([shivaram](https://github.com/shivaram))
- \[Issue\#108\] Refactor Storage API [\#119](https://github.com/pywren/pywren/pull/119) ([ooq](https://github.com/ooq))
- fixed minor spelling mistake [\#118](https://github.com/pywren/pywren/pull/118) ([sean-smith](https://github.com/sean-smith))
- Added validation for s3 bucket names and made username portion of def… [\#117](https://github.com/pywren/pywren/pull/117) ([sean-smith](https://github.com/sean-smith))
- Fix issue with bucket creation in us-east-1 [\#113](https://github.com/pywren/pywren/pull/113) ([Donohue](https://github.com/Donohue))

## [v0.2](https://github.com/pywren/pywren/tree/v0.2) (2017-03-27)
[Full Changelog](https://github.com/pywren/pywren/compare/v0.1...v0.2)

**Closed issues:**

- Modules do not serialize in ipython notebook [\#84](https://github.com/pywren/pywren/issues/84)
- Create an example that uses wait\(\)  [\#67](https://github.com/pywren/pywren/issues/67)
- Migrate to github org [\#62](https://github.com/pywren/pywren/issues/62)
- use wait in the examples [\#58](https://github.com/pywren/pywren/issues/58)
- Add links to RISELab [\#45](https://github.com/pywren/pywren/issues/45)
- create pypi package [\#38](https://github.com/pywren/pywren/issues/38)
- Investigate using EMR as a better backend for execution for long-running jobs [\#12](https://github.com/pywren/pywren/issues/12)
- When creating the lambda we indiscriminately upload too much [\#98](https://github.com/pywren/pywren/issues/98)
- Standardize configuration for executors [\#86](https://github.com/pywren/pywren/issues/86)
- pywren not working for numba functions in 0.1 due to module serialization weirdness [\#83](https://github.com/pywren/pywren/issues/83)
- pywren not respecting non UTF-8 encoding \(if coding is provided at top of file\) [\#82](https://github.com/pywren/pywren/issues/82)
- Only \*.py in modules are uploaded [\#79](https://github.com/pywren/pywren/issues/79)
- Handle exception pickling [\#78](https://github.com/pywren/pywren/issues/78)
- Capture exception traceback from remote [\#77](https://github.com/pywren/pywren/issues/77)
- Turn on runtime sharding by default [\#75](https://github.com/pywren/pywren/issues/75)
- Why do we use multiprocess instead of multiprocessing [\#60](https://github.com/pywren/pywren/issues/60)
- Generic refactor / split wren.py / run pyflakes [\#59](https://github.com/pywren/pywren/issues/59)
- Testing for pywrencli.py [\#55](https://github.com/pywren/pywren/issues/55)
- Better synchronization of runtime information with local client [\#44](https://github.com/pywren/pywren/issues/44)
- Create S3 bucket if it doesn't exist [\#35](https://github.com/pywren/pywren/issues/35)
- Add documentation on permissions [\#27](https://github.com/pywren/pywren/issues/27)
- Fix directories so that the conda command-line utils have right path [\#18](https://github.com/pywren/pywren/issues/18)
- Create interactive getting started script [\#16](https://github.com/pywren/pywren/issues/16)

**Merged pull requests:**

- external shared s3 client [\#115](https://github.com/pywren/pywren/pull/115) ([ericmjonas](https://github.com/ericmjonas))
- Fix issue 98 [\#104](https://github.com/pywren/pywren/pull/104) ([ericmjonas](https://github.com/ericmjonas))
- properly set path and test [\#100](https://github.com/pywren/pywren/pull/100) ([ericmjonas](https://github.com/ericmjonas))
- Serialization bugs [\#99](https://github.com/pywren/pywren/pull/99) ([ericmjonas](https://github.com/ericmjonas))
- Refactor uses of config in executor. [\#97](https://github.com/pywren/pywren/pull/97) ([shivaram](https://github.com/shivaram))
- switch to multiprocessing [\#94](https://github.com/pywren/pywren/pull/94) ([ericmjonas](https://github.com/ericmjonas))
- Use S3 paginators API. [\#93](https://github.com/pywren/pywren/pull/93) ([ooq](https://github.com/ooq))
- Bug fix in s3util. [\#92](https://github.com/pywren/pywren/pull/92) ([ooq](https://github.com/ooq))
- Split wren.py [\#90](https://github.com/pywren/pywren/pull/90) ([ooq](https://github.com/ooq))
- Interactive setup script \(Issue \#16\) [\#89](https://github.com/pywren/pywren/pull/89) ([ericmjonas](https://github.com/ericmjonas))
- Move runtime sharding into config variable [\#88](https://github.com/pywren/pywren/pull/88) ([shivaram](https://github.com/shivaram))
- \[Issue\#77\] Print out traceback for exceptions from wrenhandler.py. [\#87](https://github.com/pywren/pywren/pull/87) ([ooq](https://github.com/ooq))
- fix to issue 84, modules work in interactive mode [\#85](https://github.com/pywren/pywren/pull/85) ([Vaishaal](https://github.com/Vaishaal))
- Release branch [\#81](https://github.com/pywren/pywren/pull/81) ([ericmjonas](https://github.com/ericmjonas))

## [v0.1](https://github.com/pywren/pywren/tree/v0.1) (2017-03-07)
[Full Changelog](https://github.com/pywren/pywren/compare/v0.1rc4...v0.1)



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*
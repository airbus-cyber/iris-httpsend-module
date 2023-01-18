# iris-httpsend-module

This is a plugin for incident response tool [DFIR-IRIS](https://dfir-iris.org/).
It is registered on all postload hooks (except global tasks hooks) and sends http requests to an API.

The build produces docker images with plugin iris-httpsend-module preinstalled.
To import the dockers:
```
docker load --input iris-httpsend-0.1.0.dockers.tar.gz
```

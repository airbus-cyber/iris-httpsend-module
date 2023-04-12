# iris-httpsend-module

This is a plugin for incident response tool [DFIR-IRIS](https://dfir-iris.org/).
It is registered on all postload hooks (except global tasks hooks) and sends http requests to an API.

The build produces docker images with plugin iris-httpsend-module preinstalled.
To import the dockers:
```
docker load --input iris-httpsend-${VERSION}.dockers.tar.gz
```

## Build

To build the package:
```
python setup.py bdist_wheel
```
Then copy the wheel produced in `dist` to iris-web, directory `source/dependencies`.
Enrich iris-web `source/requirements.txt` with the name of the wheel, and build the dockers:
```
docker-compose build
```
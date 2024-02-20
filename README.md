# IRIS HTTP Send Module

## License

IRIS HTTP Send Module

Copyright (C) 2023 Airbus CyberSecurity SAS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

### Third-party software usage

This program uses the following software to run:

| Software | Version | Copyright | License |
|-|-|-|-|
| DFIR-IRIS | 2^ | 2023 DFIR-IRIS | LGPL-3.0-or-later |

See repositories of third-party softwares for more information about their
dependencies.

## Description

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
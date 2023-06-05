# Changelog

All notable changes to this project will be documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.6.1](https://github.com/airbus-cyber/iris-httpsend-module/compare/0.6.0...0.6.1)
### Bug Fixes
* Set correct package version

## [0.6.0](https://github.com/airbus-cyber/iris-httpsend-module/compare/0.5.0...0.6.0)
### Features
* includes patch of DFIR-IRIS so that the request to register module (POST /manage/modules/add) returns the module information


## [0.5.0](https://github.com/airbus-cyber/iris-httpsend-module/compare/0.4.0...0.5.0)
### Features
* now registers to hook `on_postload_case_update` to handle case updates
* added field `case_id` for notes, iocs and evidences
* updated DFIR-IRIS version to v2.2.2


## [0.4.0](https://github.com/airbus-cyber/iris-httpsend-module/compare/0.3.0...0.4.0)
### Features
* added mandatory configuration parameter url
* updated DFIR-IRIS version to v2.1.0
* added a patch so that users created from ldap are automatically added to the `analyst` group


## [0.3.0](https://github.com/airbus-cyber/iris-httpsend-module/compare/0.2.0...0.3.0)
### Features
* updated DFIR-IRIS version to v2.0.0


## [0.2.0](https://github.com/airbus-cyber/iris-httpsend-module/compare/0.1.0...0.2.0)
### Features
* updated DFIR-IRIS version to v2.0.0-beta-3
* dockers are now tagged with the DFIR-IRIS version
* renamed docker iris iris-web_db into iriswebapp_db


## [0.1.0](https://github.com/airbus-cyber/iris-httpsend-module/commits/0.1.0)
### Features
* first version of the module which registers on all postload hooks to log some information about the data
* build and publish dockers of DFIR-IRIS with the module pre-installed
* based on DFIR-IRIS version v2.0.0-beta-2


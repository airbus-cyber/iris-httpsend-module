# Installation

* https://docs.dfir-iris.org/getting_started/
* to find the administrator password
  docker-compose logs | grep create_safe_admin
* login to https://127.0.0.1
* to reset everything and start afresh
  docker volume prune

# Configuration

* file .env
* administrator API KEY can be configured with variable IRIS_ADM_API_KEY
* variables CERT_FILENAME and KEY_FILENAME which are use in the nginx configuration (docker/nginx/nginx.conf)


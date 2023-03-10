# Documentation

* https://docs.dfir-iris.org/operations/api/
* https://docs.dfir-iris.org/_static/iris_api_reference_v1.0.3.html

# Usage

* Needs the API_KEY to authenticate the user.
* Requests can be performed on https://localhost, the default certificates are stored in docker/dev_certs
  ```
  curl --cacert docker/dev_certs/iris_dev_cert.pem --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json' --request GET --url https://127.0.0.1:443/api/versions
  ```
* Requests can also be performed on http://localhost:8000
  ```
  curl --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json' --request GET --url http://127.0.0.1:8000/api/versions
  ```

# Endpoints

## API version information
```
GET /api/versions
```
## Create a case
```
POST /manage/cases/add {"case_name": "Case name", "case_description": "Case description", "case_customer": <customer_identifier:int>, "case_soc_id": "" }
```
Example:
```
curl --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json' --request POST --url http://127.0.0.1:8000/manage/cases/add --data '{"case_name": "Case name", "case_description": "Case description", "case_customer": 1, "case_soc_id": "" }'
```

## Get all cases
```
GET /manage/cases/list
```

## Export a case
```
GET /case/export?cid={case_identifier}
```

## Register a module
```
POST /manage/modules/add { "module_name": <module_name:string> }
```
Example:
```
curl --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json' --request POST --url http://127.0.0.1:8000/manage/modules/add --data '{ "module_name": "iris_httpsend_module" }'
```

## Enable a module
```
POST /manage/modules/enable/{module_identifier}
```

## Configure a module
```
POST /manage/modules/import-config/{module_identifier} { "module_configuration": <module_configuration:json> }
```
The module configuration is a JSON similar to the one when clicking on export configuration.
Example:
```
curl --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json' --request POST --url http://127.0.0.1:8000/manage/modules/import-config/8 --data '{ "module_configuration": [{ "default": true, "mandatory": true, "param_description": "Logs every hook received if set to true. Otherwise do nothing.", "param_human_name": "Log received hook", "param_name": "check_log_received_hook", "type": "bool", "value": false }] }'
```
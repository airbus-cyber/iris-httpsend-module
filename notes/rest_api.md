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
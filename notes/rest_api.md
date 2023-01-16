# Documentation

* https://docs.dfir-iris.org/operations/api/
* https://docs.dfir-iris.org/_static/iris_api_reference_v1.0.3.html

# Usage

* Needs the API_KEY to authenticate the user.
* Requests can be performed on https://localhost, the default certificates are stored in docker/dev_certs
curl --cacert docker/dev_certs/iris_dev_cert.pem --request GET --url https://127.0.0.1:443/api/versions --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json'
* Requests can also be performed on http://localhost:8000
curl --request GET --url http://127.0.0.1:8000/api/versions --header 'Authorization: Bearer '${API_KEY} --header 'Content-Type: application/json'

# Endpoints

## Export a case
* /case/export?cid={case_identifier}

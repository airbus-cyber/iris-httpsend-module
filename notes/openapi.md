# OpenAPI

The API that httpsend expects to send to is specified with [OpenAPI](https://www.openapis.org/) 3. 
Some bibliography about OpenAPI:
* [Documentation](https://oai.github.io/Documentation/)
* [Map](https://openapi-map.apihandyman.io/)
* [Tools](https://tools.openapis.org/)
* [Specifications](https://spec.openapis.org/oas/v3.1.0)

# Mocking

The server can be quickly mocked with [prism](https://stoplight.io/open-source/prism).

Add this to the docker-compose:
```
  httpsend-listen:
    image: stoplight/prism:4
    command: mock -h 0.0.0.0 /prism/api.yml
    networks:
      - iris_backend
    ports:
      - '4010:4010'
    volumes:
      - ./specification:/prism
```

Module httpsend can be configured with base URL http://httpsend-listen:4010.
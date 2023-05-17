# Some development tricks

* To test out code modification, it is possible to hack into the running container:
```
docker exec -it iriswebapp_app /bin/bash
docker-compose restart && docker-compose logs --follow
```

* It's better to add mounts into the `volume` section that point to the local application source code, for both the app and the worker:
```
      - ./source/app:/iriswebapp/app
```

* This can be done without modifying the original `docker-compose.yml` file by adding a `docker-compose.override.yml` file such as [this one](docker-compose.override.yml)

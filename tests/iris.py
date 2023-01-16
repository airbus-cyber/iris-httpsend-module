import time
from rest_api import RestApi
from docker_compose import DockerCompose

_API_URL = 'http://127.0.0.1:8000'
# Assumes iris docker-compose file is started with a .env file which defines IRIS_ADM_API_KEY with this value
_API_KEY = 'B8BA5D730210B50F41C06941582D7965D57319D5685440587F98DFDC45A01594'
_DOCKER_COMPOSE_PATH = '../../iris-web'


class Iris:

    def __init__(self):
        self._api = RestApi(_API_URL, _API_KEY)
        self._docker_compose = DockerCompose(_DOCKER_COMPOSE_PATH)

    def _wait_until_api_is_ready(self):
        while not self._api.is_ready():
            time.sleep(1)

    def start(self):
        self._docker_compose.start()
        # TODO would be nicer if there were a way to be notified by the docker once it is ready to take incoming requests
        print('Waiting for DFIR-IRIS to start...')
        self._wait_until_api_is_ready()

    def stop(self):
        self._docker_compose.stop()

    def get_api_version(self):
        response = self._api.get('api/versions')
        body = response.json()
        return body['data']['api_current']

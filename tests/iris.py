# This file is part of IRIS HTTP Send Module.
#
# Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
# IRIS HTTP Send Module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# IRIS HTTP Send Module is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with IRIS HTTP Send Module. If not, see <https://www.gnu.org/licenses/>.

import tempfile
import shutil
import time
from pathlib import Path
from rest_api import RestApi
from docker_compose import DockerCompose
from server_timeout_error import ServerTimeoutError

_API_URL = 'http://127.0.0.1:8000'
# Assumes iris docker-compose file is started with a .env file which defines IRIS_ADM_API_KEY with this value
_API_KEY = 'B8BA5D730210B50F41C06941582D7965D57319D5685440587F98DFDC45A01594'
_IRIS_PATH = '../../iris-web'
_TEST_DATA_PATH = Path('./data')


class Iris:

    def __init__(self, env_file, additional_docker_compose=None):
        self._working_directory = tempfile.TemporaryDirectory(prefix='iris_', dir='.')
        self._docker_compose_path = Path(self._working_directory.name).joinpath('iris')
        self._env_file = env_file
        self._additional_docker_compose = additional_docker_compose
        self._api = RestApi(_API_URL, _API_KEY)
        self._docker_compose = DockerCompose(self._docker_compose_path)

    def _wait(self, condition, attempts, sleep_duration=1):
        count = 0
        while not condition():
            time.sleep(sleep_duration)
            count += 1
            if count > attempts:
                print('Docker compose logs: ', self._docker_compose.extract_all_logs())
                raise ServerTimeoutError()

    def _wait_until_api_is_ready(self):
        self._wait(self._api.is_ready, 60)

    def start(self):
        shutil.copytree(_IRIS_PATH, self._docker_compose_path)
        shutil.copy2(_TEST_DATA_PATH.joinpath(self._env_file), self._docker_compose_path.joinpath('.env'))
        if self._additional_docker_compose is not None:
            shutil.copy2(_TEST_DATA_PATH.joinpath(self._additional_docker_compose), self._docker_compose_path.joinpath('docker-compose.override.yml'))
        self._docker_compose.start()
        # TODO would be nicer if there were a way to be notified by the docker once it is ready to take incoming requests
        print('Waiting for DFIR-IRIS to start...')
        self._wait_until_api_is_ready()

    def stop(self):
        self._docker_compose.stop()
        self._working_directory.cleanup()

    def get_api_version(self):
        response = self._api.get('api/versions')
        body = response.json()
        return body['data']['api_current']

    def create_case(self, name, description, customer_identifier):
        body = {
            'case_name': name,
            'case_description': description,
            'case_customer': customer_identifier,
            'case_soc_id': ''
        }
        response = self._api.post('/manage/cases/add', body)
        body = response.json()
        return body['data']['case_id']

    def export_case(self, case_identifier):
        response = self._api.get('/case/export', query_parameters={'cid': case_identifier})
        body = response.json()
        return body['data']

    def get_cases_count(self):
        response = self._api.get('/manage/cases/list')
        body = response.json()
        return len(body['data'])

    def register_module(self, module_name):
        body = {
            'module_name': module_name
        }
        # TODO would be nice if this request would return the modules information or at least its identifier
        self._api.post('/manage/modules/add', body)

    def list_modules(self):
        response = self._api.get('/manage/modules/list')
        body = response.json()
        return body['data']

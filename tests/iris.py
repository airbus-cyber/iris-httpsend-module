#  Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

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

    def create_case(self, name, description, customer_identifier):
        body =  {
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

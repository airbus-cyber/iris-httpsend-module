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

import requests
from requests.exceptions import ConnectionError
from urllib import parse


class RestApi:

    def __init__(self, url, api_key):
        self._url = url
        self._api_key = api_key

    def _build_url(self, path):
        return parse.urljoin(self._url, path)

    def get(self, path, query_parameters=None):
        url = self._build_url(path)
        headers = {'Authorization': f'Bearer {self._api_key}', 'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, params=query_parameters)
        print(f'GET {url} => {response.status_code}')
        return response

    def post(self, path, payload):
        url = self._build_url(path)
        headers = {'Authorization': f'Bearer {self._api_key}', 'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, json=payload)
        print(f'POST {url} {payload} => {response.status_code}')
        return response

    def is_ready(self):
        try:
            requests.head(self._url)
            return True
        except ConnectionError:
            return False

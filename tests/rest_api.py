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

import requests
from requests.exceptions import ConnectionError
from urllib import parse


class RestApi:

    def __init__(self, url, api_key):
        self._url = url
        self._api_key = api_key

    def _build_url(self, path):
        return parse.urljoin(self._url, path)

    def get(self, path):
        url = self._build_url(path)
        headers = {'Authorization': f'Bearer {self._api_key}', 'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        print('GET {} => {}'.format(url, response.status_code))
        return response

    def is_ready(self):
        try:
            requests.head(self._url)
            return True
        except ConnectionError:
            return False

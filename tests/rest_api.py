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

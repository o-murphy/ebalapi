import logging

import requests

from .flags import UrlSchema, HttpMethod
from . import resourse

__all__ = ['CrudApiClient']

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('api_crud_client')


class CrudApiClient:
    def __init__(self, base_url: str,
                 api_version: int,
                 token: str = None,
                 schema: UrlSchema = UrlSchema.HTTP,
                 **extra_params):
        self.token = token

        self.default_params = {'token': self.token}
        self.default_params.update(extra_params)
        self.base_url = f"{schema}{base_url}/v{api_version}"
        self.session = requests.Session()

    def __getattr__(self, name):
        return resourse.Resource(self, name)

    def request(self, method: HttpMethod, url: str, **extra_params) -> [dict | requests.Response]:
        params = self.default_params.copy()
        log.info(url)

        request = self.session.request
        if method == HttpMethod.GET:
            params.update(extra_params)
            response = request(method, url, params=params)
        else:
            response = request(method, url, params=params, **extra_params)
        response.raise_for_status()
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return response


if __name__ == '__main__':
    ...

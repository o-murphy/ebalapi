import logging

import requests

from . import types
from .flags import UrlSchema, HttpMethod

__all__ = ['EBalApiClient', 'CrudApiClient']

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
        return types.Resource(self, name)

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


class EBalApiClient(CrudApiClient):
    diameters: types.DiameterResource
    calibers: types.CaliberResource
    rifles: types.RifleResource
    vendors: types.VendorResource
    bullets: types.BulletResource
    drag_functions: types.DragFunctionResource
    cartridges: types.CartridgeResource

    def login(self, username: str, password: str, **kwargs):
        result = self.session.request(
            HttpMethod.POST, f'{self.base_url}/auth/', json={"username": username, "password": password}
        )

        if not result:
            return None
        auth_data = types.AuthData(**result.json())
        self.token = auth_data.token
        log.info('Auth success')
        return auth_data

    def __init__(self,
                 base_url='127.0.0.1:8000/api',
                 api_version=1,
                 token='50dbd59b4078e42dceb65d142debd89c52106a69',
                 schema=UrlSchema.HTTP,
                 **extra_params):
        super(EBalApiClient, self).__init__(base_url, api_version, token, schema, **extra_params)


if __name__ == '__main__':
    client = EBalApiClient()
    diam = client.diameter.get(0).rifle.list()

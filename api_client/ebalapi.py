import json
from enum import StrEnum
from urllib.parse import urlencode

import requests
from requests import RequestException

from api_client.types import *


class UrlSchema(StrEnum):
    HTTP = 'http://'
    HTTPS = 'https://'


class EBalAPIError(Exception):
    """
    Exception raised when an eBallistica API call fails due to a network
    related error or for a eBallistica specific reason.
    """
    errors = {
        # 1: 'Invalid session',
        # 2: 'Invalid service',
        # 3: 'Invalid result',
        # 4: 'Invalid input',
        # 5: 'Error performing request',
        # 6: 'Unknow error',
        # 7: 'Access denied',
        # 8: 'Invalid user name or password',
        # 9: 'Authorization server is unavailable, please try again later',
        # 1001: 'No message for selected interval',
        # 1002: 'Item with such unique property already exists',
        # 1003: 'Only one request of given time is allowed at the moment'
    }

    def __init__(self, code, text):
        self._text = text
        self._code = code
        try:
            self._code = int(code)
        except ValueError:
            pass

    def __unicode__(self):
        explanation = self._text
        if self._code in EBalAPIError.errors:
            explanation = " ".join([EBalAPIError.errors[self._code], self._text])

        message = f'({self._code}) {explanation} '
        return f'{message}'

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return str(self)


class EBalAPI:
    request_headers = {
        'Accept-Encoding': 'gzip, deflate'
    }

    def __init__(self,
                 base_url: str,
                 api_version: int,
                 token: str = None,
                 schema: UrlSchema = UrlSchema.HTTP,
                 **extra_params):
        self._token = token

        self.__default_params = {}
        self.__default_params.update(extra_params)
        self.__base_url = f"{schema}{base_url.replace('//', '')}/api/v{api_version}/"

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, token: str):
        self._token = token

    def update_extra_params(self, **params):
        """
        Updated the eBallistica API default parameters.
        """
        self.__default_params.update(params)

    def call(self, action, *args, **kwargs):
        """
        Call the API method provided with the parameters supplied.
        """

        action = action.replace('_', '/')

        if len(action) < 1:
            raise ValueError(f'Invalid action name {action}')

        url = f'{self.__base_url}{action}/'

        params = self.__default_params.copy()
        if self.token:
            params.update({'token': self.token})

        if not kwargs:
            if isinstance(args, tuple) and len(args) == 1:
                pk = args[0]
                url = f'{url}{pk}/'
        else:
            params.update(kwargs)

        response = self.request(url=url, params=params)

        return self.parse(response)

    def request(self, url, params):
        print(url)
        url_params = urlencode(params)
        try:
            response = requests.get(url, params=url_params, headers=self.request_headers)
            result = response.json()

        except RequestException as error:
            response = error.response

            if not response:
                raise EBalAPIError(
                    0,
                    f"{error}, url: {url}, params: {json.dumps(params)}"
                )

            result = {'detail': str(error)}

        if not response.ok:
            raise EBalAPIError(
                response.status_code,
                f"HTTP Error: {response.reason}, url: {url}, params: {json.dumps(params)}, result: {json.dumps(result)}"
            )

        return result

    def parse(self, response: dict):

        # content_type = response.get('content_type', None)
        items = response.get('items', None)

        # if content_type:

        if items:
            response_object = []
            for item in items:
                content_type = item.get('content_type', 'EBalAPIObject')
                EBalAPIObjectClass = type(content_type.capitalize(), (AbstractEBalAPIObject,), {})
                response_object.append(EBalAPIObjectClass(self, **item))
        else:
            content_type = response.get('content_type', 'EBalAPIObject')
            EBalAPIObjectClass = type(content_type.capitalize(), (AbstractEBalAPIObject,), {})
            response_object = EBalAPIObjectClass(self, **response)
        return response_object

    def __getattr__(self, action):
        """
        Enable the calling of eBallistica API methods through Python method calls
        of the same name.
        """

        def get(self, *args, **kwargs):
            return self.call(action, *args, **kwargs)

        return get.__get__(self)

    # # TODO: create protect method
    # def protect(self, func):
    #     ...


if __name__ == '__main__':
    client = EBalAPI(
        base_url='127.0.0.1:8000', api_version=1,
        token='50dbd59b4078e42dceb65d142debd89c52106a69',
        schema=UrlSchema.HTTP,
    )

    # client.sdasa()

    caliber: Bullet = client.bullets(id=5)
    print(caliber)

    # print(caliber)

    # caliber.diameter.name = 'sada'
    # li = list(caliber.__dir__())
    # li.sort()
    # pprint(li)

from enum import StrEnum
from urllib.parse import urlencode

import requests
import validators
from requests import RequestException, JSONDecodeError


class UrlSchema(StrEnum):
    http = 'http://'
    https = 'https://'


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

        message = u'{error} ({code})'.format(error=explanation, code=self._code)
        return u'eBallisticaError({message})'.format(message=message)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return str(self)


class AbstractEBalAPIObject:

    def __init__(self, api_client: 'EBalAPI', **kwargs):
        self.__api_client = api_client
        for key, val in kwargs.items():
            if validators.url(str(val)):
                act = f"{key.replace('_url', '')}"
                self.__setattr__(
                    f'get_{act}', lambda action=act, url=val: self.__call(action, url)
                )
            else:
                self.__setattr__(key, val)

    def __call(self, action, url):
        response = self.__api_client.request(
            action, url=url,
            params={'token': self.__api_client.token}
        )

        response.update({'action': action})

        return response


class EBalAPI:
    request_headers = {
        'Accept-Encoding': 'gzip, deflate'
    }

    def __init__(self, schema: UrlSchema, base_url: str, api_version: int, token: str = None, **extra_params):
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
                raise ValueError(f'Invalid input. {action} {args, kwargs}')
        else:
            params.update(kwargs)

        response = self.request(action, url, params)
        response.update({'action': action})

        return response

    def request(self, action, url, params):
        url_params = urlencode(params)
        try:
            response = requests.get(url, params=url_params, headers=self.request_headers)
        except RequestException as exc:
            raise EBalAPIError(0, f"{exc}")

        try:
            result = response.json()
        except JSONDecodeError:
            raise EBalAPIError(0, f"HTTP {response.status_code}")

        if isinstance(result, dict) and 'detail' in result:
            raise EBalAPIError(result['detail'], action)

        return result

    def parse(self, response: dict):

        action = response.get('action', None)
        items = response.get('items', None)

        if action:
            EBalAPIObjectClass = type(action.capitalize(), (AbstractEBalAPIObject,), {})

            if items:
                return [EBalAPIObjectClass(self, **item) for item in items]

            else:

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


if __name__ == '__main__':
    client = EBalAPI(
        UrlSchema.http,
        '127.0.0.1:8000', 1,
        '50dbd59b4078e42dceb65d142debd89c52106a69'
    )

    res = client.bullets(5)

    bullet = client.parse(res)

    vendor = client.parse(bullet.get_vendor())

    vb = client.parse(vendor.get_bullets())

    print(bullet, vendor, vb[0])

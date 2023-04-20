from enum import StrEnum

try:
    from builtins import str
except:
    str = lambda x: "%s" % x

try:
    from urllib import urlencode
    from urlparse import urljoin
except Exception:
    from urllib.parse import urlencode, urljoin

try:
    from urllib2 import Request, urlopen, HTTPError, URLError
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError

try:
    import simplejson as json

    assert json  # Silence potential warnings from static analysis tools
except ImportError:
    import json


class UrlSchema(StrEnum):
    HTTP = 'http://'
    HTTPS = 'https://'


class EBalAPIError(Exception):
    """
    Exception raised when an eBallistica API call fails due to a network
    related error or for a eBallistica specific reason.
    """
    errors = {
        1: 'Invalid session',
        2: 'Invalid service',
        3: 'Invalid result',
        4: 'Invalid input',
        5: 'Error performing request',
        6: 'Unknow error',
        7: 'Access denied',
        8: 'Invalid user name or password',
        9: 'Authorization server is unavailable, please try again later',
        1001: 'No message for selected interval',
        1002: 'Item with such unique property already exists',
        1003: 'Only one request of given time is allowed at the moment'
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
        if (self._code in EBalAPIError.errors):
            explanation = " ".join([EBalAPIError.errors[self._code], self._text])

        message = u'{error} ({code})'.format(error=explanation, code=self._code)
        return u'eBallisticaError({message})'.format(message=message)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return str(self)


class EBalAPI:
    request_headers = {
        'Accept-Encoding': 'gzip, deflate'
    }

    def __init__(self, schema: UrlSchema, base_url: str, api_version: int, token: str = None, **extra_params):
        pass

    @property
    def token(self) -> str:
        pass

    @token.setter
    def token(self, token: str):
        pass

    def update_extra_params(self, **params):
        """
        Updated the eBallistica API default parameters.
        """
        pass

    def call(self, action_name, *args, **kwargs) -> dict:
        """
        Call the API method provided with the parameters supplied.
        """
        pass

    def request(self, action_name, url, params) -> dict:
        pass

    def __getattr__(self, action_name):
        """
        Enable the calling of eBallistica API methods through Python method calls
        of the same name.
        """
        pass

    def bullets(self, id: int = None, search: str = None, name: str = None, vendor: int = None, weight: float = None,
                length: float = None, diameter: int = None, diameter_value: float = None, *args,
                **kwargs) -> 'AbstractEBalAPIObject':
        """
        id: int - bullet id (optional)
        search: str - full text search string (optional)
        name: str - bullet name (optional)
        vendor: int - bullet vendor id (optional)
        weight: int - bullet weight (optional)
        length: int - bullet length (optional)
        diameter: int - bullet diameter id (optional)
        diameter_value: int - bullet diameter value (optional)
        """
        pass

    def calibers(self, id: int = None, search: str = None, name: str = None, diameter: int = None,
                 diameter_value: float = None,
                 *args, **kwargs) -> 'AbstractEBalAPIObject':
        pass

    def cartridges(self, id: int = None, search: str = None, name: str = None, vendor: int = None, caliber: int = None,
                   bullet: int = None, diameter: int = None, diameter_value: float = None,
                   *args, **kwargs) -> 'AbstractEBalAPIObject':
        pass

    def diameters(self, id: int = None, diameter: int = None, *args, **kwargs) -> 'AbstractEBalAPIObject':
        pass

    def dragfuncs(self, id: int = None, search: str = None, bullet: int = None, *args, **kwargs) -> 'AbstractEBalAPIObject':
        pass

    def rifles(self, id: int = None, search: str = None, name: str = None, vendor: int = None,
               barrel_length: float = None, rail_angle: float = None, caliber: int = None, twist_rate: float = None,
               twist_direction: int = None, diameter: int = None, diameter_value: float = None,
               *args, **kwargs) -> 'AbstractEBalAPIObject':
        pass

    def vendors(self, id: int = None, name: str = None, *args, **kwargs) -> dict:
        pass

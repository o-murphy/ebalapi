from abc import ABC
from enum import StrEnum
from typing import Iterable


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


class AbstractEBalAPIObject(ABC):

    def __init__(self, api_client: 'EBalAPI', **kwargs):
        object.__setattr__(self, '_api_client', api_client)
        for key, val in kwargs.items():
            object.__setattr__(self, key, val)

    def __new__(cls, *args, **kwargs):
        if cls is AbstractEBalAPIObject:
            raise TypeError("Cannot instantiate AbstractEBalAPIObjectABC directly.")
        return object.__new__(cls)

    def __setattr__(self, name, value):
        raise NotImplementedError(f'{self.__class__.__name__} object is immutable, use update method instead')

    def __getattr__(self, action):
        """
        Enable the calling of eBallistica API methods through Python method calls
        of the same name.
        """
        if action == '_api_client':
            return self._api_client
        return self.__call(action)
        # raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{action}'")

    @property
    def json(self):
        output: dict = {k: v for k, v in self.__dict__.items() if type(v) in [int, float, str]}
        return output

    def __dir__(self) -> Iterable[str]:
        output: Iterable = super(AbstractEBalAPIObject, self).__dir__()
        output += [key.replace('_url', '') for key in self.__dict__.keys() if key.endswith('_url')]
        return set(output)

    def __call(self, action):
        url = self.__getattribute__(f'{action}_url')
        response = self._api_client.request(url=url, params={'token': self._api_client.token})
        return self._api_client.parse(response)

    def update(self):  # TODO
        raise NotImplementedError(f'{self.__class__.__name__}.{self.update.__name__} method not implemented')

    def create(self):  # TODO
        raise NotImplementedError(f'{self.__class__.__name__}.{self.create.__name__} method not implemented')


class Bullet(AbstractEBalAPIObject):
    content_type: str
    url: str
    id: int
    name: str
    vendor_id: str
    vendor_name: str
    weight: float
    length: float
    g1: float
    g7: float
    comment: str
    diameter_id: int
    diameter_value: float

    vendor_url: str
    diameter_url: str
    cartridges_url: str
    drag_functions_url: str

    metadata: str

    @property
    def diameter(self):
        return self.diameter

    @property
    def vendor(self):
        return self.vendor

    @property
    def cartridges(self):
        return self.cartridges

    @property
    def drag_functions(self):
        return self.drag_functions


class Caliber(AbstractEBalAPIObject):
    content_type: str

    id: int
    url: str

    name: str
    short_name: str

    comment: str
    diameter_id: int
    diameter_value: float

    diameter_url: str
    rifles_url: str
    cartridges_url: str

    @property
    def cartridges(self):
        return self.cartridges

    @property
    def diameter(self):
        return self.diameter

    @property
    def rifles(self):
        return self.rifles

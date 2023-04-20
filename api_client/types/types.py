from typing import Iterable, NamedTuple
from abc import ABC, abstractmethod


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

    def __class__(self):
        return AbstractEBalAPIObject

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
        response = self._api_client.request(action, url=url, params={'token': self._api_client.token})
        return self._api_client.parse(response)

    def update(self):
        ...

    def create(self):
        ...


class Bullet(AbstractEBalAPIObject):
    content_type: str
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


from abc import ABC, abstractmethod

from .resourse import ResourceInstance, RelatedResource, Resource


class CaliberResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'CaliberInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['CaliberInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'CaliberInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'CaliberInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'CaliberInstance':
        ...


class RelatedCaliber(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'CaliberInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['CaliberInstance']:
        ...


class CaliberInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    name: str
    url: str
    short_name: str
    comment: str
    diameter: int
    diameter_id: int
    diameter_value: float
    cartridges_url: str
    rifles_url: str
    diameter_url: str

    @property
    @abstractmethod
    def rifle(self) -> 'RelatedRifle':
        ...

    @property
    @abstractmethod
    def diameter(self) -> 'RelatedDiameter':
        ...

    @property
    @abstractmethod
    def cartridge(self) -> 'RelatedCartridge':
        ...


class DiameterResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'DiameterInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['DiameterInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'DiameterInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'DiameterInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'DiameterInstance':
        ...


class RelatedDiameter(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'DiameterInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['DiameterInstance']:
        ...


class DiameterInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    diameter: float
    url: str
    calibers_url: str
    bullets_url: str
    rifles_url: str

    @property
    @abstractmethod
    def rifle(self) -> 'RelatedRifle':
        ...

    @property
    @abstractmethod
    def caliber(self) -> 'RelatedCaliber':
        ...

    @property
    @abstractmethod
    def bullet(self) -> 'RelatedBullet':
        ...


class RifleResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'RifleInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['RifleInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'RifleInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'RifleInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'RifleInstance':
        ...


class RelatedRifle(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'RifleInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['RifleInstance']:
        ...


class RifleInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    url: str
    name: str
    caliber: int
    vendor: int
    caliber_id: int
    caliber_name: str
    twist_rate: float
    twist_direction: int
    twist_direction_type: str
    diameter_value: float
    diameter_id: int
    vendor_id: int
    vendor_name: str
    barrel_length: float
    rail_angle: float
    comment: str
    vendor_url: str
    caliber_url: str

    @property
    @abstractmethod
    def vendor(self) -> 'RelatedVendor':
        ...

    @property
    @abstractmethod
    def caliber(self) -> 'RelatedCaliber':
        ...


class VendorResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'VendorInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['VendorInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'VendorInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'VendorInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'VendorInstance':
        ...


class RelatedVendor(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'VendorInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['VendorInstance']:
        ...


class VendorInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    url: str
    name: str
    cartridges_url: str
    bullets_url: str
    rifles_url: str

    @property
    @abstractmethod
    def cartridge(self) -> 'RelatedCartridge':
        ...

    @property
    @abstractmethod
    def bullet(self) -> 'RelatedBullet':
        ...

    @property
    @abstractmethod
    def rifle(self) -> 'RelatedRifle':
        ...


class BulletResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'BulletInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['BulletInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'BulletInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'BulletInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'BulletInstance':
        ...


class RelatedBullet(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'BulletInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['BulletInstance']:
        ...


class BulletInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    url: str
    name: str
    vendor_id: int
    vendor_name: str
    weight: float
    length: float
    g1: float
    g7: float
    diameter_id: int
    diameter_value: float
    comment: str

    metadata: dict

    vendor_url: str
    diameter_url: str
    drag_functions_url: str
    cartridges_url: str

    @property
    @abstractmethod
    def vendor(self) -> 'RelatedVendor':
        ...

    @property
    @abstractmethod
    def diameter(self) -> 'RelatedDiameter':
        ...

    @property
    @abstractmethod
    def drag_function(self) -> 'RelatedDragFunction':
        ...

    @property
    @abstractmethod
    def cartridge(self) -> 'RelatedCartridge':
        ...


class CartridgeResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'CartridgeInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['CartridgeInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'CartridgeInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'CartridgeInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'CartridgeInstance':
        ...


class RelatedCartridge(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'CartridgeInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['CartridgeInstance']:
        ...


class CartridgeInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    url: str
    name: str
    vendor_id: int
    vendor_name: str
    caliber_id: int
    caliber_name: str
    bullet_id: int
    bullet_name: str
    bullet_weight: float
    diameter_id: int
    diameter_value: float
    muzzle_velocity: float
    temperature: float
    temperature_sensitivity: list[dict[str, float]]
    comment: str

    caliber_url: str
    vendor_url: str
    bullet_url: str

    @property
    @abstractmethod
    def vendor(self) -> 'RelatedVendor':
        ...

    @property
    @abstractmethod
    def bullet(self) -> 'RelatedBullet':
        ...

    @property
    @abstractmethod
    def caliber(self) -> 'RelatedCaliber':
        ...


class DragFunctionResource(ABC, Resource):

    @abstractmethod
    def get(self, id: int) -> 'DragFunctionInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['DragFunctionInstance']:
        ...

    @abstractmethod
    def create(self, **extra_params) -> 'DragFunctionInstance':
        ...

    @abstractmethod
    def update(self, id: int, **extra_params) -> 'DragFunctionInstance':
        ...

    @abstractmethod
    def from_dict(self, data: dict) -> 'DragFunctionInstance':
        ...


class RelatedDragFunction(RelatedResource):

    @abstractmethod
    def get(self, id: int) -> 'DragFunctionInstance':
        ...

    @abstractmethod
    def list(self, **extra_params) -> list['DragFunctionInstance']:
        ...


class DragFunctionInstance(ABC, ResourceInstance):
    content_type: str
    id: int
    url: str
    df_type: int
    df_type_string: str
    df_data: list | dict
    bullet_id: int
    bullet_url: str
    comment: str

    @property
    @abstractmethod
    def bullet(self) -> 'RelatedBullet':
        ...


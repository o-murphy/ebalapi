from enum import StrEnum
from api_client.types.crud_client import Resource, ResourceInstance, RelatedResource

class UrlSchema(StrEnum):
    HTTP = 'http://'
    HTTPS = 'https://'


class HttpMethod(StrEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'

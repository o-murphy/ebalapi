from enum import StrEnum


class UrlSchema(StrEnum):
    HTTP = 'http://'
    HTTPS = 'https://'


class HttpMethod(StrEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'

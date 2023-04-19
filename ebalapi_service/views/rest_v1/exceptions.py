from rest_framework import status
from rest_framework.exceptions import APIException


class ApiRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def serialize(self):
        return {'code': self.status_code, 'detail': self.detail}

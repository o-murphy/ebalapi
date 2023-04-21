from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError, ErrorDetail, APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from ..token_auth import GetTokenAuthentication

import abc


class AbstractListView(abc.ABC):
    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]

    def _get_model(self):
        return self.serializer_class.Meta.model

    def list(self, request: Request, *args, **kwargs):
        try:
            model_fileds = self._get_model()._meta.get_fields()
            model_fields = [field.name for field in model_fileds]
            for rp in request.query_params:
                if rp not in model_fields:
                    raise ValidationError
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            # content = {
            #     "total": queryset.count(),
            #     "items": serializer.data
            # }
            # return Response(content)
            return Response(serializer.data)


        except ValidationError as e:
            try:
                detail_list = list(e.detail.items())
                key, value = detail_list[0]
                return Response({'detail': f'{key}: {value[0]}'}, status=status.HTTP_400_BAD_REQUEST)
            except (TypeError, KeyError, AttributeError):
                return Response({'detail': str(e)}, status=e.status_code)
        except APIException as e:
            return Response({'detail': str(e)}, status=e.status_code)

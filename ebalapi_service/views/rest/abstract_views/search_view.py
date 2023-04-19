from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from ..token_auth import GetTokenAuthentication

import abc


class AbstractSearchView(abc.ABC):
    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_model(self):
        return self.serializer_class.Meta.model

    def list(self, request: Request, *args, **kwargs):
        try:
            model_fileds = self.get_model()._meta.get_fields()
            model_fields = [field.name for field in model_fileds]
            model_fields.append('search')
            for rp in request.query_params:
                if rp not in model_fields:
                    raise ValidationError
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            content = {
                "totalItems": queryset.count(),
                "items": serializer.data
            }
            return Response(content)

        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

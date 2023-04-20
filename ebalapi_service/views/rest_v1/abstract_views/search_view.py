from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError, ErrorDetail
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

    def _get_model(self):
        return self.serializer_class.Meta.model

    def list(self, request: Request, *args, **kwargs):
        try:
            fileds = ['search', 'token']

            if hasattr(self, 'filterset_class'):
                fileds += self.filterset_class.Meta.fields
            elif hasattr(self, 'filterset_fields'):
                fileds += self.filterset_fields

            for rp in request.query_params:
                if rp not in fileds:
                    raise ValidationError(detail=f'Invalid input. field: {rp}')

            queryset: QuerySet = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            content = {
                "total": queryset.count(),
                # "model": self._get_model()._meta.model_name,  # TODO: get models or get types
                "items": serializer.data,
            }
            return Response(content)

        except ValidationError as e:
            try:
                detail_list = list(e.detail.items())
                key, value = detail_list[0]
                return Response({'detail': f'{key}: {value[0]}'}, status=status.HTTP_400_BAD_REQUEST)
            except (TypeError, KeyError):
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

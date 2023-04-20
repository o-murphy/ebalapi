import abc

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..token_auth import GetTokenAuthentication


class AbstractDetailView(abc.ABC):
    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

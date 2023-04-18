from django_filters import NumberFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ebalapi_service.models import Cartridge
from .serializers import CartridgeSerializer, CartridgeDetailSerializer
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes

from .token_auth import GetTokenAuthentication


class CartridgeDetailView(RetrieveAPIView):
    name = 'Caliber Detail'

    queryset = Cartridge.objects.all()
    serializer_class = CartridgeDetailSerializer
    # lookup_field = 'pk'


class CartridgeSearchView(generics.ListAPIView):

    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]

    serializer_class = CartridgeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'name', 'vendor', 'caliber', 'bullet', ]
    search_fields = ['name', 'comment', 'vendor__name', 'caliber__name', 'bullet__name', 'caliber__short_name']
    queryset = Cartridge.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        content = {
            "totalItems": queryset.count(),
            "items": serializer.data
        }
        return Response(content)

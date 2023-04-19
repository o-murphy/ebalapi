from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

from ebalapi_service.models import Cartridge
from .abstract_views import AbstractDetailView, AbstractSearchView
from .serializers import CartridgeSerializer, CartridgeDetailSerializer


class CartridgeDetailView(AbstractDetailView, RetrieveAPIView):
    name = 'Cartridge Detail'

    queryset = Cartridge.objects.all()
    serializer_class = CartridgeDetailSerializer
    # lookup_field = 'pk'


class CartridgeSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Cartridge Search'

    serializer_class = CartridgeSerializer
    filterset_fields = ['id', 'name', 'vendor', 'caliber', 'bullet', ]
    search_fields = ['name', 'comment', 'vendor__name', 'caliber__name', 'bullet__name', 'caliber__short_name']
    queryset = Cartridge.objects.all()

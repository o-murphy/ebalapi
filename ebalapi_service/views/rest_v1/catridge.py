from django_filters import NumberFilter, FilterSet
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

from ebalapi_service.models import Cartridge
from .abstract_views import AbstractDetailView, AbstractSearchView
from .serializers import CartridgeSerializer, CartridgeDetailSerializer


class CartridgeFilter(FilterSet):
    diameter_value = NumberFilter(field_name='caliber__diameter__diameter', label='Diameter')
    diameter = NumberFilter(field_name='caliber__diameter', label='Diameter')

    class Meta:
        model = Cartridge
        fields = ['id', 'name', 'vendor', 'caliber', 'bullet', 'diameter', 'diameter_value']


class CartridgeDetailView(AbstractDetailView, RetrieveAPIView):
    name = 'Cartridge Detail'

    queryset = Cartridge.objects.all()
    serializer_class = CartridgeDetailSerializer
    # lookup_field = 'pk'


class CartridgeSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Cartridge Search'

    serializer_class = CartridgeSerializer
    filterset_class = CartridgeFilter
    search_fields = ['name', 'vendor__name', 'caliber__name', 'bullet__name', 'caliber__short_name']
    queryset = Cartridge.objects.all()

from django_filters import NumberFilter, FilterSet

from ebalapi_service.models import Cartridge
from .abstract import AbstractDetailView, AbstractSearchView
from .serializers import CartridgeSerializer


class CartridgeFilter(FilterSet):
    diameter_value = NumberFilter(field_name='caliber__diameter__diameter', label='Diameter')
    diameter = NumberFilter(field_name='caliber__diameter', label='Diameter')

    class Meta:
        model = Cartridge
        fields = ['id', 'name', 'vendor', 'caliber', 'bullet', 'diameter', 'diameter_value']


class CartridgeDetailView(AbstractDetailView):
    name = 'Cartridge Detail'

    queryset = Cartridge.objects.all()
    serializer_class = CartridgeSerializer
    # lookup_field = 'pk'


class CartridgeSearchView(AbstractSearchView):
    name = 'Cartridge Search'

    serializer_class = CartridgeSerializer
    filterset_class = CartridgeFilter
    search_fields = ['name', 'vendor__name', 'caliber__name', 'bullet__name', 'caliber__short_name']
    queryset = Cartridge.objects.all()

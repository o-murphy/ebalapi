from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet

from ebalapi_service.models import Rifle
from .abstract import AbstractDetailView, AbstractSearchView
from .serializers import RifleSerializer


class RifleFilter(FilterSet):
    diameter = NumberFilter(field_name='caliber__diameter', label='Diameter')
    diameter_value = NumberFilter(field_name='caliber__diameter__diameter', label='Diameter')

    class Meta:
        model = Rifle
        fields = ['id', 'name', 'vendor', 'barrel_length', 'rail_angle', 'caliber', 'twist_rate',
                  'twist_direction', 'diameter',
                  'diameter_value']


class RifleDetailView(AbstractDetailView):
    name = 'Rifle Detail'

    serializer_class = RifleSerializer
    queryset = Rifle.objects.all()
    # lookup_field = 'pk'


class RifleSearchView(AbstractSearchView):
    name = 'Rifle Search'

    serializer_class = RifleSerializer
    filterset_class = RifleFilter
    search_fields = ['name', 'vendor__name', 'caliber__name', 'caliber__short_name']
    queryset = Rifle.objects.all()

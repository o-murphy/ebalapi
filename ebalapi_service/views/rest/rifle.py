from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet
from rest_framework import generics

from ebalapi_service.models import Rifle
from .abstract_views import AbstractDetailView, AbstractSearchView
from .serializers import RifleSerializer, RifleDetailSerializer


class RifleFilter(FilterSet):
    cdid = NumberFilter(field_name='caliber__diameter', label='Diameter')
    cdd = NumberFilter(field_name='caliber__diameter__diameter', label='Diameter')

    class Meta:
        model = Rifle
        fields = ['id', 'name', 'vendor', 'barrel_length', 'rail_angle', 'caliber', 'twist_rate',
                  'twist_direction', 'caliber__diameter',
                  'caliber__diameter__diameter']


class RifleDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Rifle Detail'

    serializer_class = RifleDetailSerializer
    queryset = Rifle.objects.all()
    # lookup_field = 'pk'


class RifleSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Rifle Search'

    serializer_class = RifleSerializer
    filterset_class = RifleFilter
    search_fields = ['name', 'comment', 'vendor__name', 'caliber__name', 'caliber__short_name']
    queryset = Rifle.objects.all()

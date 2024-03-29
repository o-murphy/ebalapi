from django_filters import NumberFilter, FilterSet
from rest_framework import generics

from ebalapi_service.models import Caliber
from .abstract import AbstractDetailView, AbstractSearchView
from .serializers import CaliberSerializer


class CaliberFilter(FilterSet):
    diameter_value = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'diameter', 'diameter_value', ]


class CaliberDetailView(AbstractDetailView):
    name = 'Caliber Detail'

    queryset = Caliber.objects.all()
    serializer_class = CaliberSerializer
    # lookup_field = 'pk'


class CaliberSearchView(AbstractSearchView):
    name = 'Caliber Search'

    serializer_class = CaliberSerializer
    filterset_class = CaliberFilter
    search_fields = ['name', 'short_name']
    queryset = Caliber.objects.all()

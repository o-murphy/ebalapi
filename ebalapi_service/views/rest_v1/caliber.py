from django_filters import NumberFilter, FilterSet
from rest_framework import generics

from ebalapi_service.models import Caliber
from .abstract_views import AbstractDetailView, AbstractSearchView
from .serializers import CaliberSerializer, CaliberDetailSerializer


class CaliberFilter(FilterSet):
    diameter_value = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'diameter', 'diameter_value', ]


class CaliberDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Caliber Detail'

    queryset = Caliber.objects.all()
    serializer_class = CaliberDetailSerializer
    # lookup_field = 'pk'


class CaliberSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Caliber Search'

    serializer_class = CaliberSerializer
    filterset_class = CaliberFilter
    search_fields = ['name', 'short_name']
    queryset = Caliber.objects.all()

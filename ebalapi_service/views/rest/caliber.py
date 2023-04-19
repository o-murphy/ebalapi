from django_filters import NumberFilter, FilterSet
from rest_framework import generics

from ebalapi_service.models import Caliber
from .abstract_views import AbstractDetailView, AbstractSearchView
from .serializers import CaliberSerializer, CaliberDetailSerializer


class CaliberFilter(FilterSet):
    dd = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'diameter', 'diameter__diameter', ]


class CaliberDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Caliber Detail'

    queryset = Caliber.objects.all()
    serializer_class = CaliberDetailSerializer
    # lookup_field = 'pk'


class CaliberSearchView(generics.ListAPIView, AbstractSearchView):
    name = 'Caliber Search'

    serializer_class = CaliberSerializer
    filterset_class = CaliberFilter
    # filterset_fields = ['id', 'name', 'diameter', 'diameter__diameter', ]
    search_fields = ['name', 'comment', 'short_name']
    queryset = Caliber.objects.all()

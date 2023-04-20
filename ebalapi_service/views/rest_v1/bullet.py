from django_filters import FilterSet, NumberFilter
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from ebalapi_service.models import Bullet
from .abstract import AbstractSearchView, AbstractDetailView, AbstractListView
from .serializers import BulletSerializer


class BulletFilter(FilterSet):
    diameter_value = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Bullet
        fields = ['id', 'name', 'vendor', 'diameter', 'diameter_value', 'weight', 'length']


class BulletDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Bullet Detail'

    serializer_class = BulletSerializer
    queryset = Bullet.objects.all()
    # lookup_field = 'pk'


class BulletSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Bullet Search'

    serializer_class = BulletSerializer
    filterset_class = BulletFilter
    search_fields = ['name', 'vendor__name']
    queryset = Bullet.objects.all()

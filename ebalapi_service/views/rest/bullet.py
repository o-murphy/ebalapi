from django_filters import FilterSet, NumberFilter
from rest_framework import generics

from ebalapi_service.models import Bullet
from .abstract_views import AbstractSearchView, AbstractDetailView
from .serializers import BulletSerializer, BulletDetailSerializer


class BulletFilter(FilterSet):
    dd = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Bullet
        fields = ['id', 'name', 'vendor', 'diameter', 'diameter__diameter', 'weight', 'length']


class BulletDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Bullet Detail'

    serializer_class = BulletDetailSerializer
    queryset = Bullet.objects.all()
    # lookup_field = 'pk'


class BulletSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Bullet Search'

    serializer_class = BulletSerializer
    filterset_class = BulletFilter
    search_fields = ['name', 'comment', 'vendor__name']
    queryset = Bullet.objects.all()

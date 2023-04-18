from django_filters import FilterSet, NumberFilter
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ebalapi_service.models import Bullet
from .serializers import BulletSerializer


class BulletFilter(FilterSet):
    dd = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Bullet
        fields = ['id', 'diameter']


class BulletSearchListView(generics.ListAPIView):
    serializer_class = BulletSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BulletFilter
    filterset_fields = ['id', 'vendor', 'diameter', 'diameter__diameter', 'weight', 'length']
    search_fields = ['name', 'comment', 'vendor__name']
    queryset = Bullet.objects.all()

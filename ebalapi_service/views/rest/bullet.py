from django_filters import FilterSet, NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response

from ebalapi_service.models import Bullet
from .serializers import BulletSerializer, BulletDetailSerializer


class BulletFilter(FilterSet):
    dd = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Bullet
        fields = ['id', 'diameter']


class BulletDetailView(generics.RetrieveAPIView):
    serializer_class = BulletDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    queryset = Bullet.objects.all()
    # lookup_field = 'pk'


class BulletSearchView(generics.ListAPIView):
    serializer_class = BulletSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BulletFilter
    filterset_fields = ['id', 'name', 'vendor', 'diameter', 'diameter__diameter', 'weight', 'length']
    search_fields = ['name', 'comment', 'vendor__name']
    queryset = Bullet.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        content = {
            "totalItems": queryset.count(),
            "items": serializer.data
        }
        return Response(content)

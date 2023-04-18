from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ebalapi_service.models import Bullet
from .serializers import BulletSerializer


class BulletSearchListView(generics.ListAPIView):
    serializer_class = BulletSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'vendor', 'diameter', 'weight', 'length']
    search_fields = ['name', 'comment', 'vendor__name']
    queryset = Bullet.objects.all()

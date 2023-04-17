from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ebalapi_service.models import Cartridge
from .serializers import CartridgeSerializer


class CartridgeSearchListView(generics.ListAPIView):
    serializer_class = CartridgeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['vendor__id', 'bullet__id', 'caliber__id']
    search_fields = ['id', 'name', 'comment', 'vendor__name', 'bullet__name', 'caliber__name']
    queryset = Cartridge.objects.all()

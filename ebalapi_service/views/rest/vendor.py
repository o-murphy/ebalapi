from rest_framework import generics

from ebalapi_service.models import Vendor
from .abstract_views import AbstractDetailView, AbstractListView
from .serializers import VendorSerializer, VendorDetailSerializer


class VendorDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Vendor Detail'

    serializer_class = VendorDetailSerializer
    queryset = Vendor.objects.all()
    # lookup_field = 'pk'


class VendorSearchView(AbstractListView, generics.ListAPIView):
    name = 'Vendor Search'

    serializer_class = VendorSerializer
    filterset_fields = ['id', 'name']
    queryset = Vendor.objects.all()

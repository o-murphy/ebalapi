from rest_framework.generics import RetrieveAPIView

from ebalapi_service.models import Vendor
from .abstract_view import AbstractListItemView, AbstractCRUDView
from .serializers import VendorSerializer, VendorDetailSerializer


class VendorCRUDView(AbstractCRUDView):
    serializer_class = VendorDetailSerializer
    queryset = Vendor.objects.all()


class VendorView(AbstractListItemView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorDetailView(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    lookup_field = 'id'

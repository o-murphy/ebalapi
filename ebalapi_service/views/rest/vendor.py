from .abstract_view import AbstractListItemView, AbstractCRUDView
from .serializers import VendorSerializer, VendorDetailSerializer
from ebalapi_service.models import Vendor


class VendorCRUDView(AbstractCRUDView):
    serializer_class = VendorDetailSerializer
    queryset = Vendor.objects.all()


class VendorView(AbstractListItemView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

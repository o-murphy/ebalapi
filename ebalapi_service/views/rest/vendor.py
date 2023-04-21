from ebalapi_service.models import Vendor
from .abstract import AbstractDetailView, AbstractSearchView
from .serializers import VendorSerializer


class VendorDetailView(AbstractDetailView):
    name = 'Vendor Detail'

    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    # lookup_field = 'pk'


class VendorSearchView(AbstractSearchView):
    name = 'Vendor Search'

    serializer_class = VendorSerializer
    filterset_fields = ['id', 'name']
    search_fields = ['name']
    queryset = Vendor.objects.all()

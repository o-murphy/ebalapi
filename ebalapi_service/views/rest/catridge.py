from ebalapi_service.models import Cartridge
from .abstract_view import AbstractCRUDView, AbstractListItemView
from .serializers import CartridgeSerializer, CartridgeDetailSerializer


class CartridgeCRUDView(AbstractCRUDView):
    serializer_class = CartridgeDetailSerializer
    queryset = Cartridge.objects.all()


class CartridgeView(AbstractListItemView):
    serializer_class = CartridgeSerializer
    queryset = Cartridge.objects.all()

from ebalapi_service.models import Rifle
from .abstract_view import AbstractCRUDView, AbstractListItemView

from .serializers import RifleSerializer, RifleDetailSerializer


class RifleCRUDView(AbstractCRUDView):
    serializer_class = RifleDetailSerializer
    queryset = Rifle.objects.all()


class RifleView(AbstractListItemView):
    serializer_class = RifleSerializer
    queryset = Rifle.objects.all()

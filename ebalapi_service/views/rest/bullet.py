from ebalapi_service.models import Bullet
from .abstract_view import AbstractCRUDView, AbstractListItemView
from .serializers import BulletSerializer, BulletDetailSerializer


class BulletCRUDView(AbstractCRUDView):
    serializer_class = BulletDetailSerializer
    queryset = Bullet.objects.all()


class BulletView(AbstractListItemView):
    serializer_class = BulletSerializer
    queryset = Bullet.objects.all()

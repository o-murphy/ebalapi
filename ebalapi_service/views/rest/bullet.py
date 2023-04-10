from rest_framework import serializers

from ebalapi_service.models import Bullet
from .abstract_view import AbstractCRUDView, AbstractListItemView


class BulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bullet
        fields = (
            'id',
            'name',
            'vendor',
            'weight',
            'length',
            'g1',
            'g7',
            'diameter',
            'comment',
            'drag_functions',
            'cartridges'
        )


class BulletCRUDView(AbstractCRUDView):
    serializer_class = BulletSerializer
    queryset = Bullet.objects.all()


class BulletView(AbstractListItemView):
    serializer_class = BulletSerializer
    queryset = Bullet.objects.all()

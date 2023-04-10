from rest_framework import serializers

from ebalapi_service.models import Bullet, Cartridge, CartridgeVendor, Caliber, Diameter, DragFunction
from .abstract_view import AbstractCRUDView, AbstractListItemView
from .drag_function import DragFunctionInfoSerializer


# TODO: temporary
class DiameterSerialize(serializers.ModelSerializer):
    class Meta:
        model = Diameter
        fields = ('id', 'diameter')


# TODO: temporary
class CartridgeVendorSerialize(serializers.ModelSerializer):
    class Meta:
        model = CartridgeVendor
        fields = ('id', 'name', 'comment')


# TODO: temporary
class CartSerialize(serializers.ModelSerializer):

    # vendor = CartridgeVendorSerialize(many=False, read_only=True)
    # caliber = CaliberSerialize(many=False, read_only=True)

    class Meta:
        model = Cartridge
        fields = ('id', 'name', 'vendor', 'comment', 'muzzle_velocity', 'temperature', 'caliber')


class BulletListSerializer(serializers.ModelSerializer):

    # diameter = DiameterSerialize(many=False, read_only=True)
    # cartridges = CartSerialize(many=True, read_only=True)
    # drag_functions = DragFunctionSerialize(many=True, read_only=True)

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
            'cartridges',
        )


class BulletSerializer(serializers.ModelSerializer):

    diameter = DiameterSerialize(many=False, read_only=True)
    cartridges = CartSerialize(many=True, read_only=True)
    drag_functions = DragFunctionInfoSerializer(many=True, read_only=True)

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
            'cartridges',
        )


class BulletCRUDView(AbstractCRUDView):
    serializer_class = BulletSerializer
    queryset = Bullet.objects.all()


class BulletView(AbstractListItemView):
    serializer_class = BulletListSerializer
    queryset = Bullet.objects.all()

from rest_framework import serializers

from ebalapi_service.models import Bullet
from .drag_function import DragFunctionSerializer
from .diameter import DiameterSerializer


class BulletSerializer(serializers.ModelSerializer):

    diameter = DiameterSerializer(many=False, read_only=True)

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


class BulletDetailSerializer(serializers.ModelSerializer):

    diameter = DiameterSerializer(many=False, read_only=True)
    #TODO: cartridges = CartSerialize(many=True, read_only=True)
    drag_functions = DragFunctionSerializer(many=True, read_only=True)

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

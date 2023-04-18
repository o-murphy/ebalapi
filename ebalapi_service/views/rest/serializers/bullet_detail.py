from rest_framework import serializers

from ebalapi_service.models import Bullet
from .custom_fields import HyperlinkedBackRefField
from .drag_function import DragFunctionSerializer
from .diameter import DiameterSerializer
from ebalapi_service.views.rest.serializers.catridge import CartridgeSerializer


class BulletDetailSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:bullet-detail',
        # lookup_field='pk'
    )

    diameter = DiameterSerializer(many=False, read_only=True)
    cartridges = CartridgeSerializer(many=True, read_only=True)
    drag_functions = DragFunctionSerializer(many=True, read_only=True)
    metadata = serializers.JSONField(read_only=True)

    drag_functions_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:drag_function-search',
        read_only=True,
        lookup_field='bullet',
        # source='pk',
    )

    cartridges_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:cartridge-search',
        read_only=True,
        lookup_field='bullet',
        # source='pk',
    )

    class Meta:
        model = Bullet
        fields = (
            'id',
            'url',
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
            'drag_functions_url',
            'cartridges_url',
            'metadata'
        )

from rest_framework import serializers

from ebalapi_service.models import Bullet
from .diameter import DiameterSerializer
from .catridge import CartridgeLinkSerializer


class BulletSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:bullet-detail', lookup_field='id')

    diameter = DiameterSerializer(many=False, read_only=True)

    # cartridges = CartridgeLinkSerializer(many=True, read_only=True)

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
        )

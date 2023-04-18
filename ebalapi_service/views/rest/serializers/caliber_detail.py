from rest_framework import serializers

from ebalapi_service.models import Caliber

from ebalapi_service.views.rest.serializers.diameter import DiameterSerializer
from ebalapi_service.views.rest.serializers.rifle import RifleSerializer
from ebalapi_service.views.rest.serializers.catridge import CartridgeSerializer


class CaliberDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:caliber-detail',
        # lookup_field='pk'
    )

    rifles = RifleSerializer(many=True, read_only=True)
    diameter = DiameterSerializer(many=False, read_only=True)
    cartridges = CartridgeSerializer(many=True, read_only=True)

    class Meta:
        model = Caliber
        fields = ['id', 'url', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']

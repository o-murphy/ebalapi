from rest_framework import serializers

from ebalapi_service.models import Cartridge


class CartridgeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:cartridge-detail',
        # lookup_field='pk'
    )

    class Meta:
        model = Cartridge
        fields = ('id', 'url', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature',
                  'temperature_sensitivity', 'comment')

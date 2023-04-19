from rest_framework import serializers

from ebalapi_service.models import Cartridge


class CartridgeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:cartridge-detail',
        # lookup_field='pk'
    )

    vendor_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:vendor-detail',
        read_only=True,
        # lookup_field='pk',
        source='vendor',
    )

    bullet_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:bullet-detail',
        read_only=True,
        # lookup_field='pk',
        source='bullet',
    )

    caliber_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:caliber-detail',
        read_only=True,
        # lookup_field='pk',
        source='caliber',
    )

    class Meta:
        model = Cartridge
        fields = ('id', 'url', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature',
                  'temperature_sensitivity', 'caliber_url', 'vendor_url', 'bullet_url', 'comment')

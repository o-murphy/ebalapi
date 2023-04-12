from rest_framework import serializers

from ebalapi_service.models import Cartridge
from ebalapi_service.views.rest.serializers.vendor import VendorSerializer
from ebalapi_service.views.rest.serializers.caliber import CaliberSerializer
from ebalapi_service.views.rest.serializers.bullet_detail import BulletDetailSerializer


class CartridgeDetailSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:cartridge-detail', lookup_field='id')

    vendor = VendorSerializer(many=False, read_only=True)
    caliber = CaliberSerializer(many=False, read_only=True)
    bullet = BulletDetailSerializer(many=False, read_only=True)

    class Meta:
        model = Cartridge
        fields = ('id', 'url', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature',
                  'temperature_sensitivity', 'comment')

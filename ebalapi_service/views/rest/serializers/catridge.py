from rest_framework import serializers

from ebalapi_service.models import Cartridge
from ebalapi_service.views.rest.serializers.vendor import VendorSerializer
from ebalapi_service.views.rest.serializers.caliber import CaliberSerializer
from ebalapi_service.views.rest.serializers.bullet import BulletDetailSerializer


class CartridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartridge
        fields = ('id', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature',
                  'temperature_sensitivity', 'comment')


class CartridgeDetailSerializer(serializers.ModelSerializer):

    vendor = VendorSerializer(many=False, read_only=True)
    caliber = CaliberSerializer(many=False, read_only=True)
    bullet = BulletDetailSerializer(many=False, read_only=True)

    class Meta:
        model = Cartridge
        fields = ('id', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature',
                  'temperature_sensitivity', 'comment')

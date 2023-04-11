from rest_framework import serializers
from ebalapi_service.models import Vendor
from .rifle import RifleSerializer
from .bullet import BulletSerializer
from .catridge import CartridgeSerializer


class VendorDetailSerializer(serializers.ModelSerializer):

    cartridges = CartridgeSerializer(many=True, read_only=True)
    bullets = BulletSerializer(many=True, read_only=True)
    rifles = RifleSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'comment', 'cartridges', 'bullets', 'rifles',)

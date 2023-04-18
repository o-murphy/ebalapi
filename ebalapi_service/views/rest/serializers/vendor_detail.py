from rest_framework import serializers

from ebalapi_service.models import Vendor
from .bullet import BulletSerializer
from .catridge import CartridgeSerializer
from .rifle import RifleSerializer


class VendorDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:vendor-detail',
        # lookup_field='pk'
    )

    cartridges = CartridgeSerializer(many=True, read_only=True)
    bullets = BulletSerializer(many=True, read_only=True)
    rifles = RifleSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = ('id', 'url', 'name', 'comment', 'cartridges', 'bullets', 'rifles',)

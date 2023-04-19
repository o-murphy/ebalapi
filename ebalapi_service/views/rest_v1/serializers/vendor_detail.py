from rest_framework import serializers

from ebalapi_service.models import Vendor
from .bullet import BulletSerializer
from .catridge import CartridgeSerializer
from .custom_fields import HyperlinkedBackRefField
from .rifle import RifleSerializer


class VendorDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:vendor-detail',
        # lookup_field='pk'
    )

    cartridges = CartridgeSerializer(many=True, read_only=True)
    bullets = BulletSerializer(many=True, read_only=True)
    rifles = RifleSerializer(many=True, read_only=True)

    bullets_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:bullet-search',
        read_only=True,
        lookup_field='vendor',
        source='pk',
    )

    class Meta:
        model = Vendor
        fields = ('id', 'url', 'name', 'comment', 'cartridges', 'bullets', 'rifles', 'bullets_url')

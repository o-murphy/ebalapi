from rest_framework import serializers
from ebalapi_service.models import Vendor
from .rifle import RifleSerializer


class VendorDetailSerializer(serializers.ModelSerializer):
    # TODO:
    # cartridges
    # bullets
    rifles = RifleSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'comment', 'cartridges', 'bullets', 'rifles',)

from rest_framework import serializers

from ebalapi_service.models import Vendor
from ebalapi_service.views.rest_v1.serializers.custom_fields import HyperlinkedBackRefField


class VendorSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='ebalapi_service:vendor-detail',
    #     # lookup_field='pk'
    # )

    model_name = serializers.SerializerMethodField(read_only=True)

    def get_model_name(self, obj: Vendor):
        return obj._meta.model_name

    bullets_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:bullet-search',
        read_only=True,
        lookup_field='vendor',
        source='pk',
    )

    rifles_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:rifle-search',
        read_only=True,
        lookup_field='vendor',
        source='pk',
    )

    cartridges_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:cartridge-search',
        read_only=True,
        lookup_field='vendor',
        source='pk',
    )

    class Meta:
        model = Vendor
        fields = ('model_name',
                  'id',
                  # 'url',
                  'name', 'comment',
                  'cartridges_url',
                  'bullets_url',
                  'rifles_url',)

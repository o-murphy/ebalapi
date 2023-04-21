from rest_framework import serializers


from ebalapi_service.models import Bullet
from .custom_fields import HyperlinkedBackRefField


class BulletSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:bullet-detail',
        # lookup_field='id'
    )

    content_type = serializers.SerializerMethodField(read_only=True)

    vendor_name = serializers.SerializerMethodField(read_only=True)
    diameter_value = serializers.SerializerMethodField(read_only=True)

    def get_content_type(self, obj: Bullet):
        return obj._meta.model_name

    def get_vendor_name(self, obj: Bullet):
        return obj.vendor.name

    def get_diameter_value(self, obj: Bullet):
        return obj.diameter.diameter

    diameter_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:diameter-detail',
        read_only=True,
        # lookup_field='pk',
        source='diameter',
    )
    vendor_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:vendor-detail',
        read_only=True,
        # lookup_field='pk',
        source='diameter',
    )

    drag_functions_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:drag_function-search',
        read_only=True,
        lookup_field='bullet',
        source='pk',
    )

    cartridges_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:cartridge-search',
        read_only=True,
        lookup_field='bullet',
        source='pk',
    )

    class Meta:
        model = Bullet
        fields = (
            'content_type',
            'id',
            'url',
            'name',
            'vendor_id',
            'vendor_name',
            'weight',
            'length',
            'g1',
            'g7',
            'diameter_id',
            'diameter_value',
            'comment',
            'vendor_url',
            'diameter_url',
            'drag_functions_url',
            'cartridges_url',
            'metadata'
        )

        write_only_fields = (
            'vendor',
            'diameter',
        )

from rest_framework import serializers

from ebalapi_service.models import Rifle
from ebalapi_service.views.rest_v1.serializers.caliber import CaliberSerializer
from ebalapi_service.views.rest_v1.serializers.vendor import VendorSerializer


class RifleSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='ebalapi_service:rifle-detail',
    #     # lookup_field='pk'
    # )

    content_type = serializers.SerializerMethodField(read_only=True)
    twist_direction_type = serializers.SerializerMethodField(read_only=True)

    vendor_name = serializers.SerializerMethodField(read_only=True)
    caliber_name = serializers.SerializerMethodField(read_only=True)
    diameter_id = serializers.SerializerMethodField(read_only=True)
    diameter_value = serializers.SerializerMethodField(read_only=True)

    def get_vendor_name(self, obj: Rifle):
        return obj.vendor.name if obj.vendor else None

    def get_caliber_name(self, obj: Rifle):
        return obj.caliber.name if obj.caliber else None

    def get_diameter_id(self, obj: Rifle):
        if obj.caliber:
            if obj.caliber.diameter:
                return obj.caliber.diameter_id
        return

    def get_diameter_value(self, obj: Rifle):
        if obj.caliber:
            if obj.caliber.diameter:
                return obj.caliber.diameter.diameter
        return

    def get_content_type(self, obj: Rifle):
        return obj._meta.model_name

    def get_twist_direction_type(self, obj: Rifle):
        return obj.TwistDirection(obj.twist_direction).name

    vendor_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:vendor-detail',
        read_only=True,
        # lookup_field='pk',
        source='vendor',
    )

    caliber_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:caliber-detail',
        read_only=True,
        # lookup_field='pk',
        source='caliber',
    )

    class Meta:
        model = Rifle
        fields = (
            'content_type',
            'id',
            # 'url',
            'name',
            'caliber_id',
            'caliber_name',
            'twist_rate',
            'twist_direction',
            'twist_direction_type',
            'diameter_value',
            'diameter_id',
            'vendor_id',
            'vendor_name',
            'barrel_length',
            'rail_angle',
            'comment',
            'vendor_url',
            'caliber_url',
        )


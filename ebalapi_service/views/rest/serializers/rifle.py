from rest_framework import serializers

from ebalapi_service.models import Rifle
from ebalapi_service.views.rest.serializers.caliber import CaliberSerializer
from ebalapi_service.views.rest.serializers.vendor import VendorSerializer


class RifleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:rifle-detail', lookup_field='id')

    twist_direction_type = serializers.SerializerMethodField(read_only=True)

    def get_twist_direction_type(self, obj: Rifle):
        return obj.TwistDirection(obj.twist_direction).name

    class Meta:
        model = Rifle
        fields = ('id', 'url', 'name', 'caliber', 'twist_rate', 'twist_direction', 'twist_direction_type', 'vendor',
                  'barrel_length', 'rail_angle',
                  'comment')


class RifleDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:rifle-detail', lookup_field='id')

    twist_direction_type = serializers.SerializerMethodField(read_only=True)

    vendor = VendorSerializer(many=False, read_only=True)
    caliber = CaliberSerializer(many=False, read_only=True)

    def get_twist_direction_type(self, obj: Rifle):
        return obj.TwistDirection(obj.twist_direction).name

    class Meta:
        model = Rifle
        fields = ('id', 'url', 'name', 'caliber', 'twist_rate', 'twist_direction', 'twist_direction_type', 'vendor',
                  'barrel_length', 'rail_angle',
                  'comment')

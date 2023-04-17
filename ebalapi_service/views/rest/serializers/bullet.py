from rest_framework import serializers

from ebalapi_service.models import Bullet


# from ebalapi_service.views.rest.serializers import VendorSerializer
# from .diameter import DiameterSerializer


class BulletSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:bullet-detail', lookup_field='id')

    vendor_name = serializers.SerializerMethodField(read_only=True)
    diameter_value = serializers.SerializerMethodField(read_only=True)

    def get_vendor_name(self, obj: Bullet):
        return obj.vendor.name

    def get_diameter_value(self, obj: Bullet):
        return obj.diameter.diameter

    diameter_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:diameter-detail',
        read_only=True,
        lookup_field='id',
        source='diameter',
    )

    # diameter = DiameterSerializer(many=False, read_only=True)

    # cartridges = CartridgeLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Bullet
        fields = (
            'id',
            'url',
            'name',
            'vendor',
            'vendor_name',
            'weight',
            'length',
            'g1',
            'g7',
            'diameter',
            'diameter_value',
            'diameter_url',
            'comment',
            'drag_functions',
            'cartridges',
            # 'metadata'
        )

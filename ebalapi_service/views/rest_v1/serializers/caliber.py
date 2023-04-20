from rest_framework import serializers

from ebalapi_service.models import Caliber
from ebalapi_service.views.rest_v1.diameter import DiameterSerializer
from .custom_fields import HyperlinkedBackRefField


class CaliberSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='ebalapi_service:caliber-detail',
    #     # lookup_field='pk'
    # )

    # diameter = DiameterSerializer(many=False, read_only=True)

    content_type = serializers.SerializerMethodField(read_only=True)

    diameter_value = serializers.SerializerMethodField(read_only=True)

    def get_content_type(self, obj: Caliber):
        return obj._meta.model_name

    def get_diameter_value(self, obj: Caliber):
        return obj.diameter.diameter

    diameter_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:diameter-detail',
        read_only=True,
        # lookup_field='pk',
        source='diameter',
    )

    cartridges_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:cartridge-search',
        read_only=True,
        lookup_field='caliber',
        source='pk',
    )

    rifles_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:rifle-search',
        read_only=True,
        lookup_field='caliber',
        source='pk',
    )

    class Meta:
        model = Caliber
        fields = (
            'content_type',
            'id',
            # 'url',
            'name', 'short_name', 'comment',
            'diameter_id', 'diameter_value',
            'cartridges_url',
            'rifles_url',
            'diameter_url',
            'comment'
        )

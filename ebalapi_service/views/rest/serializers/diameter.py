from rest_framework import serializers

from ebalapi_service.models import Diameter
from .custom_fields import HyperlinkedBackRefField


class DiameterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:diameter-detail',
        # lookup_field='pk'
    )

    content_type = serializers.SerializerMethodField(read_only=True)

    def get_content_type(self, obj: Diameter):
        return obj._meta.model_name

    calibers_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:caliber-search',
        read_only=True,
        lookup_field='diameter',
        source='pk',
    )

    bullets_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:bullet-search',
        read_only=True,
        lookup_field='diameter',
        source='pk',
    )

    rifles_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:rifle-search',
        read_only=True,
        lookup_field='diameter',
        source='pk',
    )

    class Meta:
        model = Diameter
        fields = (
            'content_type',
            'id',
            'url',
            'diameter',
            'calibers_url',
            'bullets_url',
            'rifles_url',
        )

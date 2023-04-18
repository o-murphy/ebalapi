from rest_framework import serializers

from ebalapi_service.models import Caliber
from ebalapi_service.views.rest.diameter import DiameterSerializer
from .custom_fields import HyperlinkedBackRefField


class CaliberSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:caliber-detail', lookup_field='id')

    diameter = DiameterSerializer(many=False, read_only=True)

    cartridges_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:cartridge-search',
        read_only=True,
        lookup_field='caliber',
        source='id',
    )

    rifles_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:rifle-search',
        read_only=True,
        lookup_field='caliber',
        source='id',
    )

    class Meta:
        model = Caliber
        fields = ['id', 'url', 'name', 'short_name', 'comment', 'diameter', 'cartridges_url', 'rifles_url']

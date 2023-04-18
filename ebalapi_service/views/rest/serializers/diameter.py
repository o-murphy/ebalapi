from django.urls import reverse
from rest_framework import serializers

from ebalapi_service.models import Diameter, Caliber
from ..custom_fields import HyperlinkedBackRefField




class DiameterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:diameter-detail', lookup_field='id')

    calibers_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:caliber-search',
        read_only=True,
        lookup_field='diameter',
        source='id',
    )

    bullets_url = HyperlinkedBackRefField(
        view_name='ebalapi_service:bullet-search',
        read_only=True,
        lookup_field='diameter',
        source='id',
    )

    class Meta:
        model = Diameter
        fields = ('id', 'url', 'diameter', 'calibers_url', 'bullets_url')

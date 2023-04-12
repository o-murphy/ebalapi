from rest_framework import serializers

from ebalapi_service.models import Caliber
from ebalapi_service.views.rest.diameter import DiameterSerializer


class CaliberSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:caliber-detail', lookup_field='id')

    diameter = DiameterSerializer(many=False, read_only=True)

    class Meta:
        model = Caliber
        fields = ['id', 'url', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']

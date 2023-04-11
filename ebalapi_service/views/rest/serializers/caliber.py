from rest_framework import serializers

from ebalapi_service.models import Caliber
from ebalapi_service.views.rest.diameter import DiameterSerializer


class CaliberSerializer(serializers.ModelSerializer):
    diameter = DiameterSerializer(many=False, read_only=True)

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']

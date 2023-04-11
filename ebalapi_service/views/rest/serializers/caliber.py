from rest_framework import serializers

from ebalapi_service.models import Caliber
from ebalapi_service.views.rest.bullet import DiameterSerialize


class CaliberSerializer(serializers.ModelSerializer):
    diameter = DiameterSerialize(many=False, read_only=True)

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']

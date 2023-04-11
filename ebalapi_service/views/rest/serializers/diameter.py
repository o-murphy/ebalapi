from rest_framework import serializers

from ebalapi_service.models import Diameter


class DiameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diameter
        fields = ('id', 'diameter', 'calibers', 'bullets')


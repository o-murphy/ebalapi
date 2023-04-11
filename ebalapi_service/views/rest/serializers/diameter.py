from rest_framework import serializers
from ebalapi_service.models import Diameter


class DiameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diameter
        fields = ('id', 'diameter', 'comment', 'calibers', 'bullets')


class DiameterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diameter
        fields = ('id', 'diameter', 'comment', 'calibers', 'bullets')

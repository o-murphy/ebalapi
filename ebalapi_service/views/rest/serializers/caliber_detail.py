from rest_framework import serializers

from ebalapi_service.models import Caliber

from ebalapi_service.views.rest.bullet import DiameterSerialize
from ebalapi_service.views.rest.serializers.rifle import RifleSerializer


class CaliberDetailSerializer(serializers.ModelSerializer):

    rifles = RifleSerializer(many=True, read_only=True)
    diameter = DiameterSerialize(many=False, read_only=True)
    #TODO: cartridges = CartSerialize(many=True, read_only=True)

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']

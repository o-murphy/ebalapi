from rest_framework import serializers
from ebalapi_service.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'comment', 'cartridges', 'bullets', 'rifles',)
from rest_framework import serializers
from ebalapi_service.models import Bullet


class BulletSearchSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name')

    class Meta:
        model = Bullet
        fields = '__all__'

from rest_framework import serializers
from rest_framework.reverse import reverse

from ebalapi_service.models import Vendor


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vendor-detail', lookup_field='id')

    class Meta:
        model = Vendor
        fields = ('id', 'url', 'name', 'comment', 'cartridges', 'bullets', 'rifles',)



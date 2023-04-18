from rest_framework import serializers

from ebalapi_service.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:vendor-detail',
        # lookup_field='pk'
    )

    class Meta:
        model = Vendor
        fields = ('id', 'url', 'name', 'comment',
                  'cartridges',
                  'bullets',
                  'rifles',
                  )

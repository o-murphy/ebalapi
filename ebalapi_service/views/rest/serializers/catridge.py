from rest_framework import serializers

from ebalapi_service.models import Cartridge


class CartridgeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:cartridge-detail',
        # lookup_field='pk'
    )

    content_type = serializers.SerializerMethodField(read_only=True)

    bullet_name = serializers.SerializerMethodField(read_only=True)
    bullet_weight = serializers.SerializerMethodField(read_only=True)
    vendor_name = serializers.SerializerMethodField(read_only=True)
    caliber_name = serializers.SerializerMethodField(read_only=True)
    diameter_id = serializers.SerializerMethodField(read_only=True)
    diameter_value = serializers.SerializerMethodField(read_only=True)

    def get_content_type(self, obj: Cartridge):
        return obj._meta.model_name

    def get_bullet_name(self, obj: Cartridge):
        return obj.bullet.name

    def get_bullet_weight(self, obj: Cartridge):
        return obj.bullet.weight

    def get_vendor_name(self, obj: Cartridge):
        return obj.vendor.name

    def get_caliber_name(self, obj: Cartridge):
        return obj.caliber.name

    def get_diameter_id(self, obj: Cartridge):
        return obj.caliber.diameter_id

    def get_diameter_value(self, obj: Cartridge):
        return obj.caliber.diameter.diameter

    vendor_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:vendor-detail',
        read_only=True,
        # lookup_field='pk',
        source='vendor',
    )

    bullet_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:bullet-detail',
        read_only=True,
        # lookup_field='pk',
        source='bullet',
    )

    caliber_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:caliber-detail',
        read_only=True,
        # lookup_field='pk',
        source='caliber',
    )

    class Meta:
        model = Cartridge
        fields = ('content_type',
                  'id',
                  'url',
                  'name',
                  'vendor_id',
                  'vendor_name',
                  'caliber_id',
                  'caliber_name',
                  'bullet_id',
                  'bullet_name',
                  'bullet_weight',
                  'diameter_id',
                  'diameter_value',
                  'muzzle_velocity',
                  'temperature',
                  'temperature_sensitivity',
                  'caliber_url',
                  'vendor_url',
                  'bullet_url',
                  'comment')

        write_only_fields = (
            'vendor',
            'caliber',
            'bullet',
        )
from watson import search as watson

from ebalapi_service.models import Cartridge


class CartridgeSearchAdapter(watson.SearchAdapter):
    name = 'Cartridge'

    def get_model(self):
        return Cartridge

    def get_description(self, obj):
        return self.get_model()._meta.verbose_name_plural.title()

    def get_queryset(self, obj):
        return obj.select_related('vendor', 'bullet', 'caliber')
        # return super().get_queryset().select_related('vendor')

    def get_indexed_fields(self):
        fields = (
            'name',
            'vendor__name',
            'bullet__name',
            'caliber__name',
            'comment',
            # 'metadata',
        )
        return fields

watson.register(Cartridge, CartridgeSearchAdapter)

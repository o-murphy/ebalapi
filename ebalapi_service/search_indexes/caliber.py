from watson import search as watson
from ebalapi_service.models import Caliber


class CaliberSearchAdapter(watson.SearchAdapter):
    name = 'Caliber'

    def get_model(self):
        return Caliber

    def get_description(self, obj):
        return self.get_model()._meta.verbose_name_plural.title()

    def get_indexed_fields(self):
        fields = (
            'name',
            'short_name',
            'comment',
        )
        return fields

watson.register(Caliber, CaliberSearchAdapter)

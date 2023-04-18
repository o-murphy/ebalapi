from watson import search as watson
import re
from ebalapi_service.models import Bullet


class BulletSearchAdapter(watson.SearchAdapter):
    name = 'Bullet'

    def get_model(self):
        return Bullet

    def get_description(self, obj):
        return self.get_model()._meta.verbose_name_plural.title()

    def get_queryset(self, obj):
        return obj.select_related('vendor')
        # return super().get_queryset().select_related('vendor')

    def get_indexed_fields(self):
        fields = (
            'name',
            'vendor__name',
            'comment',
            # 'metadata',
        )
        return fields

    # def prepare(self, obj):
    #     prepared_data = super().prepare(obj)
    #     # Remove punctuation from indexed fields
    #     for field in ['name', 'comment']:
    #         text = prepared_data[field]
    #         no_punc_text = re.sub(r'[^\w\s]', '', text)
    #         prepared_data[f"{field}_no_punc"] = no_punc_text
    #     return prepared_data

watson.register(Bullet, BulletSearchAdapter)

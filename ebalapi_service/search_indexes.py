from watson import search as watson

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

watson.register(Bullet, BulletSearchAdapter)


# print('indexes building')
# watson.register(Bullet, fields=(
#     'name',
#     'vendor',
#     'comment',
#     # 'metadata',
# ))

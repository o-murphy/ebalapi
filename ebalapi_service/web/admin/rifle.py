from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .tools import create_rel_link

# Register your models here.

from ebalapi_service.models import Rifle


@admin.register(Rifle)
class RifleAdmin(ImportExportModelAdmin):

    def _caliber(self, obj: Rifle):
        if obj.caliber:
            url = obj.caliber.get_absolute_url()
            return create_rel_link(url, obj.caliber.name)
        return f'{obj.caliber.name}'

    _caliber.admin_order_field = 'caliber'
    _caliber.short_description = "Caliber"

    list_display = (
        'id', 'name', 'barrel_length', 'rail_angle',
        'twist_direction', '_caliber'
    )

    list_display_links = ['id', 'name']

    list_filter = (
        'id', 'name', 'barrel_length', 'rail_angle',
        'twist_direction'
    )

    search_fields = (
        'name',
        '_caliber'
    )

    fieldsets = (
        (
            'Main Data', {
                'fields': ('name', 'barrel_length', 'rail_angle', 'twist_direction', 'caliber')
            }
        ),
        (
            'Comment', {
                'fields': ('comment',)
            }
        ),
    )

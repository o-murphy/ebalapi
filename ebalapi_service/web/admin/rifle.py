from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Rifle
from .tools import create_rel_link


# Register your models here.


class RifleInline(admin.StackedInline):
    extra = 0
    model = Rifle
    verbose_name = "Rifles"
    verbose_name_plural = "Rifles"
    fields = (
        'id', 'name', 'barrel_length', 'rail_angle',
        'twist_direction'
    )
    readonly_fields = (
        'id', 'name', 'barrel_length', 'rail_angle',
        'twist_direction'
    )


@admin.register(Rifle)
class RifleAdmin(ImportExportModelAdmin):

    def _caliber(self, obj: Rifle):
        if obj.caliber:
            url = obj.caliber.get_absolute_url()
            return create_rel_link(url, obj.caliber.name)
        return

    _caliber.admin_order_field = 'caliber'
    _caliber.short_description = "Caliber"

    def _vendor(self, obj: Rifle):
        if obj.vendor:
            url = obj.vendor.get_absolute_url()
            return create_rel_link(url, obj.vendor.name)
        return

    _vendor.admin_order_field = 'vendor'
    _vendor.short_description = "Vendor"

    list_display = (
        'id', 'name', 'barrel_length', 'rail_angle',
        'twist_direction', '_caliber', '_vendor'
    )

    list_display_links = ['id', 'name']

    ordering = ('id',)

    list_filter = (
        'id', 'name', 'barrel_length', 'rail_angle',
        'twist_direction'
    )

    search_fields = (
        'name',
        '_caliber',
        '_vendor'
    )

    fieldsets = (
        (
            'Main Data', {
                'fields': ('name', 'barrel_length', 'rail_angle', 'twist_direction', 'caliber', 'vendor', 'comment',)
            }
        ),
    )

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Cartridge
from .tools import create_rel_link


# Register your models here.


class CartridgeStackedInline(admin.TabularInline):
    extra = 0
    model = Cartridge
    verbose_name = "Cartridges"
    verbose_name_plural = "Cartridges"
    # fields = (
    #     'id', 'name'
    # )


@admin.register(Cartridge)
class CartridgeAdmin(ImportExportModelAdmin):

    def _vendor(self, obj: Cartridge):
        if obj.vendor:
            url = obj.vendor.get_absolute_url()
            return create_rel_link(url, obj.vendor.name)
        return f'{obj.vendor.name}'

    def _caliber(self, obj: Cartridge):
        if obj.caliber:
            url = obj.caliber.get_absolute_url()
            return create_rel_link(url, obj.caliber.name)
        return f'{obj.caliber.name}'

    def _bullet(self, obj: Cartridge):
        if obj.caliber:
            url = obj.bullet.get_absolute_url()
            return create_rel_link(url, obj.bullet.name)
        return f'{obj.bullet.name}'

    _caliber.admin_order_field = 'caliber'
    _caliber.short_description = "Caliber"

    _bullet.admin_order_field = 'bullet'
    _bullet.short_description = "Bullet"

    list_display_links = ['name']

    list_display = (
        'name', '_vendor', '_caliber', '_bullet', 'muzzle_velocity',
        'temperature', 'temperature_sensitivity'
    )

    list_filter = (
        'id', 'name', 'caliber'
    )

    search_fields = (
        'name',
        'caliber', 'bullet'
    )

    fieldsets = (
        (
            'Main Data', {
                'fields': (
                    'name',
                    'vendor',
                    'muzzle_velocity',
                    'temperature',
                    'temperature_sensitivity',
                    'caliber',
                    'bullet',
                )
            }
        ),
        (
            'Comment', {
                'fields': ('comment',)
            }
        ),
    )

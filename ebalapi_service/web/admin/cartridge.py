from django.contrib import admin
from django.forms import ModelForm
from django_ace import AceWidget
from import_export.admin import ImportExportModelAdmin
from watson.admin import SearchAdmin

from ebalapi_service.models import Cartridge
from .tools import create_rel_link


# Register your models here.

class CartridgeAdminForm(ModelForm):
    class Meta:
        model = Cartridge
        fields = '__all__'

        # widgets = {
        #     'temperature_sensitivity': Textarea(attrs={'cols': 40, 'rows': 1}),
        # }
        widgets = {
            'temperature_sensitivity': AceWidget(
                mode='json',
                width="400px",
                height="25px",
                theme="twilight"
            ),
        }


class CartridgeInline(admin.TabularInline):
    extra = 0
    model = Cartridge
    verbose_name = "Cartridges"
    verbose_name_plural = "Cartridges"
    fields = (
        'id', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature', 'temperature_sensitivity'
    )
    readonly_fields = (
        'id', 'name', 'vendor', 'caliber', 'bullet', 'muzzle_velocity', 'temperature', 'temperature_sensitivity')
    form = CartridgeAdminForm


@admin.register(Cartridge)
class CartridgeAdmin(
    SearchAdmin,
    ImportExportModelAdmin
):
    form = CartridgeAdminForm

    def _vendor(self, obj: Cartridge):
        if obj.vendor:
            url = obj.vendor.get_absolute_url()
            return create_rel_link(url, obj.vendor.name)
        return

    def _caliber(self, obj: Cartridge):
        if obj.caliber:
            url = obj.caliber.get_absolute_url()
            return create_rel_link(url, obj.caliber.name)
        return

    def _bullet(self, obj: Cartridge):
        if obj.caliber:
            url = obj.bullet.get_absolute_url()
            return create_rel_link(url, obj.bullet.name)
        return

    _caliber.admin_order_field = 'caliber'
    _caliber.short_description = "Caliber"

    _bullet.admin_order_field = 'bullet'
    _bullet.short_description = "Bullet"

    list_display_links = ['id', 'name']

    list_display = (
        'id', 'name', '_vendor', '_caliber', '_bullet', 'muzzle_velocity',
        'temperature', 'temperature_sensitivity'
    )

    ordering = ('id',)

    list_filter = (
        'name', 'caliber'
    )

    search_fields = (
        'name',
        'caliber__name',
        'bullet__name',
        'vendor__name',
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
                    'comment',
                )
            }
        ),
    )

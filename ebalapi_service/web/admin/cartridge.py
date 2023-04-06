from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Cartridge


# Register your models here.


class CartridgeAdmin(ImportExportModelAdmin):

    list_display_links = ['name']

    list_display = (
        'name', 'vendor', 'muzzle_velocity', 'caliber', 'bullet',
        'temperature', 'temperature_sensitivity'
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
    )

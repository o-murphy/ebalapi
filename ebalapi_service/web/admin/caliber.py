from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Caliber
from .rifle import RifleStackedInline
from .cartridge import CartridgeStackedInline
from .rifle import RifleStackedInline


@admin.register(Caliber)
class RifleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'short_name')

    inlines = [RifleStackedInline, CartridgeStackedInline]

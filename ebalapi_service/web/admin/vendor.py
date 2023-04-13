from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Vendor
from .bullet import BulletInline
from .cartridge import CartridgeInline
from .rifle import RifleInline


@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')

    list_display_links = ('id', 'name')

    ordering = ('id',)

    search_fields = ('name',)
    list_filter = ('name',)

    fields = ('name', 'comment')

    inlines = [BulletInline, CartridgeInline, RifleInline]

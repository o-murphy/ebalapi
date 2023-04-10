from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import CartridgeVendor
from .cartridge import CartridgeInline


@admin.register(CartridgeVendor)
class CartridgeVendorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')

    list_display_links = ('id', 'name')

    search_fields = ('name',)
    list_filter = ('name',)

    fields = ('name', 'comment')

    inlines = [CartridgeInline]

from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Caliber
from .cartridge import CartridgeInline
from .rifle import RifleInline


@admin.register(Caliber)
class RifleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'short_name', 'diameter')

    list_display_links = ('id', 'name', 'short_name')

    ordering = ('id',)

    search_fields = ('name', 'diameter')
    list_filter = ('name', 'diameter')

    fields = ('name', 'short_name', 'diameter', 'comment')

    inlines = [RifleInline, CartridgeInline]

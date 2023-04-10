from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import BulletVendor
from .bullet import BulletInline


@admin.register(BulletVendor)
class BulletVendorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')

    list_display_links = ('id', 'name')

    search_fields = ('name',)
    list_filter = ('name',)

    fields = ('name', 'comment')

    inlines = [BulletInline]

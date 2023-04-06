from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Bullet
from .cartridge import CartridgeStackedInline


class BulletStackedInline(admin.StackedInline):
    extra = 0
    model = Bullet
    verbose_name = "Bullets"
    verbose_name_plural = "Bullets"
    fields = (
        'id', 'name'
    )


@admin.register(Bullet)
class BulletAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name',
        'diameter'
    )

    inlines = [CartridgeStackedInline]

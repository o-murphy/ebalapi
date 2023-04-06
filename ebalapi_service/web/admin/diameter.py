from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Diameter
from .bullet import BulletStackedInline


@admin.register(Diameter)
class DiameterAdmin(ImportExportModelAdmin):
    list_display = ('id', 'diameter')

    inlines = [BulletStackedInline]

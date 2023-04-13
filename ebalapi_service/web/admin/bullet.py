from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import Bullet
from .cartridge import CartridgeInline
from .drag_function import DragFunctionInline
from .tools import create_rel_link


class BulletInline(admin.TabularInline):
    extra = 0
    model = Bullet
    verbose_name = "Bullets"
    verbose_name_plural = "Bullets"
    fields = (
        'id', 'name', 'vendor', 'weight', 'length', 'g1', 'g7', 'diameter'
    )
    readonly_fields = ('id', 'name', 'vendor', 'weight', 'length', 'g1', 'g7', 'diameter')


@admin.register(Bullet)
class BulletAdmin(ImportExportModelAdmin):

    def _vendor(self, obj: Bullet):
        if obj.vendor:
            url = obj.vendor.get_absolute_url()
            return create_rel_link(url, obj.vendor.name)
        return

    def _has_drag_functions(self, obj: Bullet):
        if obj.drag_functions.count() > 0:
            return True
        else:
            return False

    _vendor.admin_order_field = 'vendor'
    _vendor.short_description = "Vendor"

    _has_drag_functions.short_description = "Drag Funcs"
    _has_drag_functions.admin_order_field = "drag_functions"
    _has_drag_functions.boolean = True

    list_display = (
        'id', 'name', '_vendor', 'weight', 'length', 'g1', 'g7', 'diameter', '_has_drag_functions'
    )

    list_display_links = ['id', 'name']

    search_fields = (
        'id', 'name'
    )

    list_filter = ('id', 'name', 'vendor', 'weight', 'diameter')
    # sortable_by = ('drag_functions', )

    fieldsets = (
        (
            'Main Data', {
                'fields': ('name', 'vendor', 'weight', 'length', 'g1', 'g7', 'diameter', 'comment',)
            }
        ),
    )

    inlines = [CartridgeInline, DragFunctionInline]

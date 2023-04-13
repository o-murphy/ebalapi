from django.contrib import admin
# Register your models here.
from django.forms import ModelForm
from django_ace import AceWidget
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import DragFunction
from ebalapi_service.web.admin.tools import create_rel_link


class DragFunctionAdminForm(ModelForm):
    class Meta:
        model = DragFunction
        fields = '__all__'

        # widgets = {
        #     'temperature_sensitivity': Textarea(attrs={'cols': 40, 'rows': 1}),
        # }
        widgets = {
            'df_data': AceWidget(
                mode='json',
                width="400px",
                height="25px",
                theme="twilight"
            ),
        }


class DragFunctionInline(admin.TabularInline):
    extra = 0
    model = DragFunction
    verbose_name = "DragFunctions"
    verbose_name_plural = "DragFunctions"
    fields = ('id', 'name',
              'bullet',
              'df_type',
              'df_data',)
    readonly_fields = ('id', 'name',
                       'bullet',
                       'df_type',
                       'df_data',)
    form = DragFunctionAdminForm


@admin.register(DragFunction)
class CartridgeAdmin(ImportExportModelAdmin):
    form = DragFunctionAdminForm

    def _bullet(self, obj: DragFunction):
        if obj.bullet:
            url = obj.bullet.get_absolute_url()
            return create_rel_link(url, obj.bullet.name)
        return f'{obj.bullet.name}'

    _bullet.admin_order_field = 'bullet'
    _bullet.short_description = "Bullet"

    list_display_links = ['id', 'name']

    list_display = (
        'id', 'name', '_bullet', 'df_type'
    )

    ordering = ('id',)

    list_filter = (
        'id', 'name', 'bullet', 'df_type'
    )

    search_fields = (
        'id', 'name', 'bullet',
    )

    fieldsets = (
        (
            'Main Data', {
                'fields': (
                    'name',
                    'bullet',
                    'df_type',
                    'df_data',
                    'comment'
                )
            }
        ),
    )

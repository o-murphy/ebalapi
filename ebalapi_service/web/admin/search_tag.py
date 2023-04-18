from django.contrib import admin
# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.forms import BaseGenericInlineFormSet
from django.contrib.contenttypes.models import ContentType
from django.forms import HiddenInput
from import_export.admin import ImportExportModelAdmin

from ebalapi_service.models import SearchTag
from ebalapi_service.web.admin.tools import create_rel_link


class SearchTagInlineFormSet(BaseGenericInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = self.queryset.order_by('id')


class SearchTagInline(GenericTabularInline):
    model = SearchTag
    extra = 0
    formset = SearchTagInlineFormSet


@admin.register(SearchTag)
class RifleAdmin(ImportExportModelAdmin):

    def _content_object(self, obj: SearchTag):
        if obj.content_object:
            url = obj.content_object.get_absolute_url()
            return create_rel_link(url, obj.content_object)
        return

    _content_object.admin_order_field = 'object'
    _content_object.short_description = "Object"

    list_display = ('id', 'text', 'content_type', 'object_id', '_content_object')

    list_display_links = ('id', 'text',)

    ordering = ('id',)

    search_fields = ('text',)
    list_filter = ('text',)

    fields = ('text', 'content_type', 'object_id', )

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.db.models import *

# Create your models here.
from django.urls import reverse


class ContentObjectManager(ContentTypeManager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('content_object')


class SearchTag(Model):
    __tablename__ = 'search_tag'
    id = AutoField(primary_key=True, unique=True)
    text = CharField(max_length=100, null=True, blank=True)

    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id', )
    content_objects = ContentObjectManager()

    def __str__(self):
        return f'{self.text or "Untitled"} ({self.content_type}:{self.object_id})'

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

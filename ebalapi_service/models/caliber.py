from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import *
from django.urls import reverse

from .diameter import Diameter

# Create your models here.
from .search_tag import SearchTag


class Caliber(Model):
    __tablename__ = 'caliber'
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, unique=True, null=False, blank=False)
    short_name = CharField(max_length=10, unique=True, null=False, blank=False)
    comment = CharField(max_length=280, blank=True, null=True)

    diameter = ForeignKey(Diameter, related_name='calibers', on_delete=SET_NULL, null=True, blank=False)
    tags = GenericRelation(SearchTag)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

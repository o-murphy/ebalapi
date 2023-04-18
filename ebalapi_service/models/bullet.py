from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import *
from django.urls import reverse

from .vendor import Vendor
from .diameter import Diameter
from .search_tag import SearchTag


# Create your models here.


class Bullet(Model):
    __tablename__ = 'bullet'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=False, blank=False)
    vendor = ForeignKey(Vendor, related_name='bullets', on_delete=SET_NULL, null=True, blank=False)
    weight = FloatField(null=False, blank=False, default=0.168)
    length = FloatField(null=False, blank=False, default=1.2)

    g1 = FloatField(null=True, blank=True, default=0.168)
    g7 = FloatField(null=True, blank=True, default=0.168)

    comment = CharField(max_length=280, blank=True, null=True)

    diameter = ForeignKey(Diameter, related_name='bullets', on_delete=SET_NULL, null=True, blank=False)

    metadata = JSONField(blank=True, null=True, default=dict())

    tags = GenericRelation(SearchTag)

    # for full text search
    # name_no_punc = CharField(max_length=40, null=True, blank=True)
    # comment_no_punc = CharField(max_length=280, null=True, blank=True)

    def __str__(self):
        if self.vendor:
            return f'{self.vendor.name} {self.name} {self.weight}'
        else:
            return f'{self.name} {self.weight}'

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

from django.db.models import *

# Create your models here.
from django.urls import reverse


class Vendor(Model):
    __tablename__ = 'vendor'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)

    comment = CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

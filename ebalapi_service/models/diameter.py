from django.db.models import *

# Create your models here.
from django.urls import reverse


class Diameter(Model):
    __tablename__ = 'diameter'
    id = AutoField(primary_key=True, unique=True)
    diameter = FloatField(unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.diameter}'

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

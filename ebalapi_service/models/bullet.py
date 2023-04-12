from django.db.models import *
from django.urls import reverse

from .vendor import Vendor
from .diameter import Diameter


# Create your models here.


class Bullet(Model):
    __tablename__ = 'bullet'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)
    vendor = ForeignKey(Vendor, related_name='bullets', on_delete=SET_NULL, null=True, blank=False)
    weight = FloatField(null=False, blank=False, default=0.168)
    length = FloatField(null=False, blank=False, default=1.2)

    g1 = FloatField(null=True, blank=True, default=0.168)
    g7 = FloatField(null=True, blank=True, default=0.168)

    comment = CharField(max_length=280, blank=True, null=True)

    diameter = ForeignKey(Diameter, related_name='bullets', on_delete=SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ebalapi_service:bullet-detail', args=[self.id])

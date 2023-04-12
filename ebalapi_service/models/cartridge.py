from django.db.models import *
from django.urls import reverse

from ebalapi_service.models import Bullet, Caliber
from .vendor import Vendor


# Create your models here.


class Cartridge(Model):
    __tablename__ = 'cartridge'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)
    vendor = ForeignKey(Vendor, related_name='cartridges', on_delete=SET_NULL, null=True, blank=False)

    comment = CharField(max_length=280, blank=True, null=True)

    muzzle_velocity = FloatField(null=False, blank=False, default=800)
    temperature = FloatField(null=False, blank=False, default=15)

    # TODO: json field height
    temperature_sensitivity = JSONField(blank=False, null=False, default=[[15, 800], [0, 790]])

    caliber = ForeignKey(Caliber, related_name='cartridges', on_delete=SET_NULL, null=True, blank=False)

    bullet = ForeignKey(Bullet, related_name='cartridges', on_delete=SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, bullet: {self.bullet.name}, diameter: {self.caliber.name}'

    def get_absolute_url(self):
        return reverse('ebalapi_service:cartridge-detail', args=[self.id])

from django.db.models import *
from django.urls import reverse

from .caliber import Caliber
from .vendor import Vendor


# Create your models here.


class Rifle(Model):
    __tablename__ = 'rifle'

    class TwistDirection(IntegerChoices):
        Right = 1, 'Right'
        Left = 2, 'Left'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)
    vendor = ForeignKey(Vendor, related_name='rifles', on_delete=SET_NULL, null=True, blank=False)


    barrel_length = FloatField(null=False, blank=False, default=61)
    rail_angle = FloatField(null=True, blank=True, default=None)

    twist_rate = FloatField(null=False, blank=False, default=10)
    twist_direction = IntegerField(choices=TwistDirection.choices,
                                   default=TwistDirection.Right,
                                   blank=False,
                                   null=False)

    caliber = ForeignKey(Caliber, related_name='rifles', on_delete=SET_NULL, null=True, blank=False)

    comment = TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

from django.db.models import *


from .caliber import Caliber
from .rifle_vendor import RifleVendor


# Create your models here.


class Rifle(Model):
    __tablename__ = 'rifle'

    class TwistDirection(IntegerChoices):
        Right = 1, 'Right'
        Left = 2, 'Left'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)
    vendor = ForeignKey(RifleVendor, related_name='rifles', on_delete=SET_NULL, null=True, blank=False)

    comment = TextField(blank=True, null=True)

    barrel_length = FloatField(null=False, blank=False, default=61)
    rail_angle = FloatField(null=False, blank=False, default=20)

    twist_rate = FloatField(null=False, blank=False, default=10)
    twist_direction = IntegerField(max_length=20,
                                   choices=TwistDirection.choices,
                                   default=TwistDirection.Right,
                                   blank=False,
                                   null=False)

    caliber = ForeignKey(Caliber, related_name='rifles', on_delete=SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/admin/ebalapi_service/rifle/{self.pk}'

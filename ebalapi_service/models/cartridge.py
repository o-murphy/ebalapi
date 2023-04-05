from django.db.models import *


from ebalapi_service.models import Bullet, Caliber


# Create your models here.


class Cartridge(Model):
    __tablename__ = 'cartridge'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)

    # TODO: temperature to velocity table
    # muzzle_velocity = FloatField(null=False, blank=False, default=800)
    # temperature = FloatField(null=False, blank=False, default=15)
    # powder_temperature_sens = IntegerField(null=False, blank=False, default=1)

    caliber = ForeignKey(Caliber, related_name='cartridges', on_delete=SET_NULL, null=True, blank=False)
    bullet = ForeignKey(Bullet, related_name='cartridges', on_delete=SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, df: {self.drag_function_type}, diameter: {self.diameter.diameter}'



from django.db.models import *
from .diameter import Diameter

# Create your models here.


class Caliber(Model):
    __tablename__ = 'caliber'
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, unique=True, null=False, blank=False)
    short_name = CharField(max_length=10, unique=True, null=False, blank=False)
    comment = TextField(blank=True, null=True)

    diameter = ForeignKey(Diameter, related_name='calibers', on_delete=SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/admin/ebalapi_service/caliber/{self.pk}'

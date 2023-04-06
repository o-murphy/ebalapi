from django.db.models import *


# Create your models here.


class RifleVendor(Model):
    __tablename__ = 'rifle_ven'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)

    def __str__(self):
        return self.name

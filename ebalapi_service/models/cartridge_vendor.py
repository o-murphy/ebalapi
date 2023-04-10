from django.db.models import *


# Create your models here.


class CartridgeVendor(Model):
    __tablename__ = 'cartridge_ven'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)

    comment = CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/admin/ebalapi_service/cartridgevendor/{self.pk}'

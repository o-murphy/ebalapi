from django.db.models import *


# Create your models here.
from django.urls import reverse


class Vendor(Model):
    __tablename__ = 'bullet_ven'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)

    comment = CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ebalapi_service:vendor-detail', args=[self.id])

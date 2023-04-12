from django.db.models import *

# Create your models here.


class Diameter(Model):
    __tablename__ = 'diameter'
    id = AutoField(primary_key=True, unique=True)
    diameter = FloatField(unique=True, null=False, blank=False)

    def __str__(self):
        return f'id: {self.id}, diameter: {self.diameter}'


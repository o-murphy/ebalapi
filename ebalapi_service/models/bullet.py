from django.db.models import *


from .diameter import Diameter
from .bullet_vendor import BulletVendor


# Create your models here.


class Bullet(Model):
    __tablename__ = 'bullet'

    class DragFunctionType(IntegerChoices):
        G1 = 1, 'G1'
        G2 = 2, 'G2'
        G5 = 3, 'G5'
        G6 = 4, 'G6'
        G7 = 5, 'G7'
        G8 = 6, 'G8'
        GS = 7, 'GS'
        GC = 8, 'GC'
        G1_MULTI_BC = 9, 'G1 MULTI BC'
        G7_MULTI_BC = 10, 'G7 MULTI BC'
        CUSTOM = 11, 'CUSTOM'

    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)
    vendor = ForeignKey(BulletVendor, related_name='bullets', on_delete=SET_NULL, null=True, blank=False)
    weight = FloatField(null=False, blank=False, default=0.168)
    length = FloatField(null=False, blank=False, default=1.2)
    comment = TextField(blank=True, null=True)

    diameter = ForeignKey(Diameter, related_name='bullets', on_delete=SET_NULL, null=True, blank=False)

    drag_function_type = CharField(max_length=20,
                                   choices=DragFunctionType.choices,
                                   default=DragFunctionType.G7,
                                   blank=False,
                                   null=False)

    drag_function_data = JSONField(blank=False, null=False, default={"value": 0.175})

    def __str__(self):
        return self.name

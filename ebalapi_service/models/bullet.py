from django.db.models import *


from ebalapi_service.models import Diameter


# Create your models here.


class Bullet(Model):
    __tablename__ = 'bullet'

    class DragFunctionType(TextChoices):
        G1 = 'G1', 'G1'
        G2 = 'G2', 'G2'
        G5 = 'G5', 'G5'
        G6 = 'G6', 'G6'
        G7 = 'G7', 'G7'
        G8 = 'G8', 'G8'
        GS = 'GS', 'GS'
        GC = 'GC', 'GC'
        G1_MULTI_BC = 'G1_MULTI_BC', 'G1_MULTI_BC'
        G7_MULTI_BC = 'G7_MULTI_BC', 'G7_MULTI_BC'
        CUSTOM = 'CUSTOM', 'CUSTOM'



    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=40, null=False, unique=True, blank=False)
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
        return f'id: {self.id}, name: {self.name}, df: {self.drag_function_type}, diameter: {self.diameter.diameter}'

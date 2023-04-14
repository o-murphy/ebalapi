from django.db.models import *
from django.urls import reverse

from .bullet import Bullet


# Create your models here.


class DragFunction(Model):
    __tablename__ = 'drag_function'

    id = AutoField(primary_key=True, unique=True)

    bullet = ForeignKey(Bullet, related_name='drag_functions', on_delete=SET_NULL, null=True, blank=False)

    comment = CharField(max_length=280, blank=True, null=True)

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

    # TODO: json field height
    df_type = IntegerField(choices=DragFunctionType.choices,
                           default=DragFunctionType.G7,
                           blank=False,
                           null=False)

    df_data = JSONField(blank=False, null=False, default={"value": 0.175})

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

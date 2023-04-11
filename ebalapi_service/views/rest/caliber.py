from rest_framework import serializers

from ebalapi_service.models import Caliber, Rifle, Diameter, Cartridge, Vendor
from .abstract_view import AbstractCRUDView, AbstractListItemView

from .serializers import VendorSerializer


# TODO: temporary
class DiameterSerialize(serializers.ModelSerializer):
    class Meta:
        model = Diameter
        fields = ('id', 'diameter')


# TODO: temporary
class RifleSerializer(serializers.ModelSerializer):

    twist_direction_type = serializers.SerializerMethodField(read_only=True)

    def get_twist_direction_type(self, obj: Rifle):
        return obj.TwistDirection(obj.twist_direction).name

    class Meta:
        model = Rifle
        fields = ('id', 'name', 'twist_rate', 'twist_direction', 'twist_direction_type', 'vendor',
                  'barrel_length', 'rail_angle',
                  'comment')


# # TODO: temporary
# class DragFunctionSerialize(serializers.ModelSerializer):
#
#     df_type_string = serializers.SerializerMethodField(read_only=True)
#
#     def get_df_type_string(self, obj: DragFunction):
#         return obj.DragFunctionType(obj.df_type).name
#
#     class Meta:
#         model = DragFunction
#         fields = ('id', 'name', 'comment', 'df_type', 'df_type_string', 'df_data')


# # TODO: temporary
# class BulletSerializer(serializers.ModelSerializer):
#
#     diameter = DiameterSerialize(many=False, read_only=True)
#     drag_functions = DragFunctionSerialize(many=True, read_only=True)
#
#     class Meta:
#         model = Bullet
#         fields = (
#             'id',
#             'name',
#             'vendor',
#             'weight',
#             'length',
#             'g1',
#             'g7',
#             'diameter',
#             'comment',
#             'drag_functions',
#             'cartridges',
#         )


# TODO: temporary
class CartSerialize(serializers.ModelSerializer):

    vendor = VendorSerializer(many=False, read_only=True)

    class Meta:
        model = Cartridge
        fields = ('id', 'name', 'vendor', 'comment', 'muzzle_velocity', 'temperature', 'caliber', 'bullet')


class CaliberListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']


# TODO: temporary
class CaliberSerializer(serializers.ModelSerializer):

    rifles = RifleSerializer(many=True, read_only=True)
    diameter = DiameterSerialize(many=False, read_only=True)
    cartridges = CartSerialize(many=True, read_only=True)

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']


class CaliberCRUDView(AbstractCRUDView):
    serializer_class = CaliberSerializer
    queryset = Caliber.objects.all()


class CaliberView(AbstractListItemView):
    serializer_class = CaliberListSerialize
    queryset = Caliber.objects.all()

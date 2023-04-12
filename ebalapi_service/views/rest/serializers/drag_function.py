from rest_framework import serializers

from ebalapi_service.models import DragFunction
from ebalapi_service.views.rest.serializers import BulletSerializer


# class DragFunctionLinkSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:rifle-detail', lookup_field='id')
#
#     df_type_string = serializers.SerializerMethodField(read_only=True)
#
#     def get_df_type_string(self, obj: DragFunction):
#         return obj.DragFunctionType(obj.df_type).name
#
#     class Meta:
#         model = DragFunction
#         fields = ('id', 'url', 'name', 'df_type_string')


class DragFunctionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:rifle-detail', lookup_field='id')

    df_type_string = serializers.SerializerMethodField(read_only=True)

    def get_df_type_string(self, obj: DragFunction):
        return obj.DragFunctionType(obj.df_type).name

    class Meta:
        model = DragFunction
        fields = ('id', 'url', 'name', 'df_type', 'df_type_string', 'df_data', 'bullet', 'comment',)


class DragFunctionDetailSerializer(serializers.ModelSerializer):
    # TODO:
    bullets = BulletSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='ebalapi_service:rifle-detail', lookup_field='id')

    df_type_string = serializers.SerializerMethodField(read_only=True)

    def get_df_type_string(self, obj: DragFunction):
        return obj.DragFunctionType(obj.df_type).name

    class Meta:
        model = DragFunction
        fields = ('id', 'url', 'name', 'df_type', 'df_type_string', 'df_data', 'bullet', 'comment',)

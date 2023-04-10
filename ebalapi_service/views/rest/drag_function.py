from rest_framework import serializers

from ebalapi_service.models import DragFunction


# TODO: temporary
class DragFunctionInfoSerializer(serializers.ModelSerializer):
    df_type_string = serializers.SerializerMethodField(read_only=True)

    def get_df_type_string(self, obj: DragFunction):
        return obj.DragFunctionType(obj.df_type).name

    class Meta:
        model = DragFunction
        fields = ('id', 'name', 'comment', 'df_type', 'df_type_string', 'df_data')

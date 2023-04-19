from rest_framework import serializers

from ebalapi_service.models import DragFunction


class DragFunctionSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='ebalapi_service:rifle-detail',
    #     # lookup_field='pk'
    # )

    model_name = serializers.SerializerMethodField(read_only=True)
    df_type_string = serializers.SerializerMethodField(read_only=True)

    def get_model_name(self, obj: DragFunction):
        return obj._meta.model_name

    def get_df_type_string(self, obj: DragFunction):
        return obj.DragFunctionType(obj.df_type).name

    class Meta:
        model = DragFunction
        fields = (
            'model_name',
            'id',
            # 'url',
            'df_type',
            'df_type_string',
            'df_data',
            'bullet',
            'comment',
        )

from rest_framework import serializers

from ebalapi_service.models import DragFunction


class DragFunctionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ebalapi_service:rifle-detail',
        # lookup_field='pk'
    )

    content_type = serializers.SerializerMethodField(read_only=True)
    df_type_string = serializers.SerializerMethodField(read_only=True)

    bullet_url = serializers.HyperlinkedRelatedField(
        view_name='ebalapi_service:bullet-detail',
        read_only=True,
        # lookup_field='pk',
        source='bullet',
    )

    def get_content_type(self, obj: DragFunction):
        return obj._meta.model_name

    def get_df_type_string(self, obj: DragFunction):
        return obj.DragFunctionType(obj.df_type).name

    class Meta:
        model = DragFunction
        fields = (
            'content_type',
            'id',
            'url',
            'df_type',
            'df_type_string',
            'df_data',
            'bullet',
            'bullet_id',
            'bullet_url',
            'comment',
        )

from rest_framework import serializers
from .abstract_view import AbstractCRUDView, AbstractListItemView
from ebalapi_service.models import Caliber


class CaliberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caliber
        fields = ['id', 'name', 'short_name', 'comment', 'diameter', 'cartridges', 'rifles']


class CaliberCRUDView(AbstractCRUDView):
    serializer_class = CaliberSerializer
    queryset = Caliber.objects.all()


class CaliberView(AbstractListItemView):
    serializer_class = CaliberSerializer
    queryset = Caliber.objects.all()

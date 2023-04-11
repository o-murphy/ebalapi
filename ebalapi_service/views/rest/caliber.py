from rest_framework import serializers

from ebalapi_service.models import Caliber
from .abstract_view import AbstractCRUDView, AbstractListItemView

from .serializers import CaliberSerializer, CaliberDetailSerializer


class CaliberCRUDView(AbstractCRUDView):
    serializer_class = CaliberDetailSerializer
    queryset = Caliber.objects.all()


class CaliberView(AbstractListItemView):
    serializer_class = CaliberSerializer
    queryset = Caliber.objects.all()

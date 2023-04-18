from rest_framework.generics import RetrieveAPIView

from ebalapi_service.models import Caliber
from .abstract_view import AbstractCRUDView, AbstractListItemView
from .serializers import CaliberSerializer, CaliberDetailSerializer


class CaliberCRUDView(AbstractCRUDView):
    name = 'Caliber Detail'

    serializer_class = CaliberDetailSerializer
    queryset = Caliber.objects.all()


class CaliberView(AbstractListItemView):
    name = 'Caliber List'

    serializer_class = CaliberSerializer
    queryset = Caliber.objects.all()


class CaliberDetailView(RetrieveAPIView):
    name = 'Caliber Detail'

    queryset = Caliber.objects.all()
    serializer_class = CaliberDetailSerializer
    # lookup_field = 'id'

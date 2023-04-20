from rest_framework import generics

from ebalapi_service.models import DragFunction
from .abstract import AbstractDetailView, AbstractSearchView
from .serializers import DragFunctionSerializer


class DragFunctionDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Drag Function Detail'

    serializer_class = DragFunctionSerializer
    queryset = DragFunction.objects.all()
    # lookup_field = 'pk'


class DragFunctionSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Drag Function Search'

    serializer_class = DragFunctionSerializer
    filterset_fields = ['id', 'bullet', ]
    search_fields = ['bullet__name', ]
    queryset = DragFunction.objects.all()

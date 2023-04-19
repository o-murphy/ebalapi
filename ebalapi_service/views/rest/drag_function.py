from rest_framework import generics

from ebalapi_service.models import DragFunction
from .abstract_views import AbstractDetailView, AbstractSearchView
from .serializers import DragFunctionSerializer, DragFunctionDetailSerializer


class DragFunctionDetailView(AbstractDetailView, generics.RetrieveAPIView):
    name = 'Drag Function Detail'

    serializer_class = DragFunctionDetailSerializer
    queryset = DragFunction.objects.all()
    # lookup_field = 'pk'


class DragFunctionSearchView(AbstractSearchView, generics.ListAPIView):
    name = 'Drag Function Search'

    serializer_class = DragFunctionSerializer
    filterset_fields = ['id', 'name', 'bullet', ]
    search_fields = ['name', 'comment', 'bullet__name', ]
    queryset = DragFunction.objects.all()

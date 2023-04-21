from ebalapi_service.models import DragFunction
from .abstract import AbstractDetailView, AbstractSearchView
from .serializers import DragFunctionSerializer


class DragFunctionDetailView(AbstractDetailView):
    name = 'Drag Function Detail'

    serializer_class = DragFunctionSerializer
    queryset = DragFunction.objects.all()
    # lookup_field = 'pk'


class DragFunctionSearchView(AbstractSearchView):
    name = 'Drag Function Search'

    serializer_class = DragFunctionSerializer
    filterset_fields = ['id', 'bullet', ]
    search_fields = ['bullet__name', ]
    queryset = DragFunction.objects.all()

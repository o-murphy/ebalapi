from .abstract_view import AbstractListItemView, AbstractCRUDView
from .serializers import DragFunctionSerializer, DragFunctionDetailSerializer
from ebalapi_service.models import DragFunction


class DragFunctionCRUDView(AbstractCRUDView):
    serializer_class = DragFunctionDetailSerializer
    queryset = DragFunction.objects.all()


class DragFunctionView(AbstractListItemView):
    serializer_class = DragFunctionSerializer
    queryset = DragFunction.objects.all()

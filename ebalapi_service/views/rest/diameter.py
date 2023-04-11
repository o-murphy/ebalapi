from .abstract_view import AbstractListItemView, AbstractCRUDView
from ebalapi_service.views.rest.serializers.diameter import DiameterSerializer
from ebalapi_service.models import Diameter


class DiameterCRUDView(AbstractCRUDView):
    serializer_class = DiameterSerializer
    queryset = Diameter.objects.all()


class DiameterView(AbstractListItemView):
    serializer_class = DiameterSerializer
    queryset = Diameter.objects.all()

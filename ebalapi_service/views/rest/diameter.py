from ebalapi_service.models import Diameter
from ebalapi_service.views.rest.serializers.diameter import DiameterSerializer
from .abstract import AbstractDetailView, AbstractListView


class DiameterDetailView(AbstractDetailView):
    name = 'Diameter Detail'

    queryset = Diameter.objects.all()
    serializer_class = DiameterSerializer
    # lookup_field = 'pk'


class DiameterSearchView(AbstractListView):
    name = 'Diameter Search'

    serializer_class = DiameterSerializer
    filterset_fields = ['id', 'diameter']
    queryset = Diameter.objects.all()

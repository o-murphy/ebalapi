from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from ebalapi_service.models import Diameter
from ebalapi_service.views.rest.serializers.diameter import DiameterSerializer


class DiameterDetailView(RetrieveAPIView):
    name = 'Diameter Detail'

    queryset = Diameter.objects.all()
    serializer_class = DiameterSerializer
    # lookup_field = 'pk'


class DiameterSearchView(generics.ListAPIView):
    serializer_class = DiameterSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ['id', 'diameter']
    queryset = Diameter.objects.all()

    def list(self, request: Request, *args, **kwargs):
        try:
            model_fields = [field.name for field in Diameter._meta.get_fields()]
            for rp in request.query_params:
                if rp not in model_fields:
                    raise ValidationError
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            content = {
                "totalItems": queryset.count(),
                "items": serializer.data
            }
            return Response(content)

        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

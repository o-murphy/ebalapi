from django_filters import NumberFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from ebalapi_service.models import Caliber
from .serializers import CaliberSerializer, CaliberDetailSerializer


class CaliberDetailView(RetrieveAPIView):
    name = 'Caliber Detail'

    queryset = Caliber.objects.all()
    serializer_class = CaliberDetailSerializer
    # lookup_field = 'pk'


class CaliberFilter(FilterSet):
    dd = NumberFilter(field_name='diameter__diameter', label='Diameter')

    class Meta:
        model = Caliber
        fields = ['id', 'diameter']


class CaliberSearchView(generics.ListAPIView):
    serializer_class = CaliberSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CaliberFilter
    filterset_fields = ['id', 'name', 'diameter', 'diameter__diameter', ]
    search_fields = ['name', 'comment', 'short_name']
    queryset = Caliber.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        content = {
            "totalItems": queryset.count(),
            "items": serializer.data
        }
        return Response(content)

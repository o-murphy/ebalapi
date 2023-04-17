from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ebalapi_service.models import Bullet
from .serializers import BulletSerializer
from django.db.models import Q


class BulletSearchListView(generics.ListAPIView):
    serializer_class = BulletSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'vendor', 'diameter', 'weight', 'length']
    search_fields = ['name', 'comment', 'vendor__name']
    queryset = Bullet.objects.all()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     # Get query params from request
    #     query_params = self.request.query_params.dict()
    #
    #     # Check if any field filters are present
    #     field_filters = {}
    #     for key, value in query_params.items():
    #         if key in self.filterset_fields:
    #             field_filters[key] = value
    #
    #     # Remove field filters from query_params
    #     for key in field_filters:
    #         del query_params[key]
    #
    #     # Apply search filter
    #     queryset = self.filter_queryset(queryset)
    #
    #     # Apply field filters
    #     if field_filters:
    #         q = Q()
    #         for key, value in field_filters.items():
    #             q &= Q(**{key: value})
    #         queryset = queryset.filter(q)
    #
    #     # Apply remaining query params as search filter
    #     if query_params:
    #         queryset = self.filter_queryset(queryset.filter(**query_params))
    #
    #     return queryset
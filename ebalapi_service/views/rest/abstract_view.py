from django.core import exceptions
from django.db.models import QuerySet
from rest_framework import exceptions as rest_exception, mixins
from rest_framework import generics
from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .token_auth import GetTokenAuthentication


class AbstractCRUDView(generics.RetrieveUpdateDestroyAPIView,
                       mixins.CreateModelMixin):

    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]
    serializer_class: serializers.ModelSerializer
    queryset: QuerySet

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):
        """
        Returns the object the view is displaying.
        """
        try:
            queryset = self.filter_queryset(self.get_queryset())
            query_params = self.request.query_params.dict()

            if isinstance(self.request.data, dict):
                query_params.update(**self.request.data)
            if not query_params:
                raise rest_exception.NotFound
            if self.request.method in ['PUT', 'PATCH']:
                obj_id = query_params.get('id')
                filter_kwargs = {"id": obj_id}
            obj = get_object_or_404(queryset, **query_params)
        except exceptions.FieldError:
            raise rest_exception.NotFound
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class AbstractListItemView(generics.ListAPIView):
    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]
    serializer_class: serializers.ModelSerializer
    queryset: QuerySet

    def get(self, request, *args, **kwargs):
        query_params = request.query_params.dict()
        if isinstance(request.data, dict):
            query_params.update(**request.data)
        try:
            items = self.queryset.filter(**query_params)
            serialized = self.serializer_class(items, many=True)
            content = {
                "totalItems": len(serialized.data),
                "items": serialized.data
            }
            return Response(content)
        except exceptions.FieldError:
            raise rest_exception.NotFound
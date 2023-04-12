from django.core import exceptions
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from rest_framework import exceptions as rest_exception, mixins, status
from rest_framework import generics
from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .token_auth import GetTokenAuthentication


# class AbstractCRUDView(generics.RetrieveUpdateDestroyAPIView,
#                        mixins.CreateModelMixin):
#
#     authentication_classes = [
#         # SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#         GetTokenAuthentication
#     ]
#     permission_classes = [IsAuthenticated]
#     serializer_class: serializers.ModelSerializer
#     queryset: QuerySet
#
#     def post(self, request: Request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def get_object(self):
#         """
#         Returns the object the view is displaying.
#         """
#         try:
#             queryset = self.filter_queryset(self.get_queryset())
#             query_params = self.request.query_params.dict()
#
#             if isinstance(self.request.data, dict):
#                 query_params.update(**self.request.data)
#             if not query_params:
#                 raise rest_exception.NotFound
#             if self.request.method in ['PUT', 'PATCH']:
#                 obj_id = query_params.get('id')
#                 filter_kwargs = {"id": obj_id}
#             obj = get_object_or_404(queryset, **query_params)
#         except exceptions.FieldError:
#             raise rest_exception.NotFound
#         # May raise a permission denied
#         self.check_object_permissions(self.request, obj)
#
#         return obj


class AbstractCRUDView(generics.RetrieveUpdateDestroyAPIView,
                       mixins.CreateModelMixin):

    serializer_class = serializers.ModelSerializer
    queryset = QuerySet

    @method_decorator(authentication_classes([BasicAuthentication, TokenAuthentication, GetTokenAuthentication]))
    @method_decorator(permission_classes([IsAuthenticated]))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())
        query_params = self.request.query_params.dict()

        # Get URL path or path list
        # path = self.request.path
        path_list = list(filter(None, self.request.path.split('/')))

        if isinstance(self.request.data, dict):
            query_params.update(**self.request.data)
        if path_list[-1].isnumeric():
            query_params.update(id=path_list[-1])
        elif not query_params:
            raise rest_exception.NotFound("Query parameters not found")

        obj_id = self.request.data.get('id')
        filter_kwargs = {"id": obj_id} if obj_id else {}

        obj = get_object_or_404(queryset, **query_params, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj


# class AbstractListItemView(generics.ListAPIView):
#     authentication_classes = [
#         # SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#         GetTokenAuthentication
#     ]
#     permission_classes = [IsAuthenticated]
#     serializer_class: serializers.ModelSerializer
#     queryset: QuerySet
#
#     def get(self, request, *args, **kwargs):
#         query_params = request.query_params.dict()
#         if isinstance(request.data, dict):
#             query_params.update(**request.data)
#         try:
#             items = self.queryset.filter(**query_params)
#             serialized = self.serializer_class(items, many=True)
#             content = {
#                 "totalItems": len(serialized.data),
#                 "items": serialized.data
#             }
#             return Response(content)
#         except exceptions.FieldError:
#             raise rest_exception.NotFound


# class AbstractListItemView(generics.ListAPIView):
#     authentication_classes = [
#         # SessionAuthentication,
#         BasicAuthentication,
#         TokenAuthentication,
#         GetTokenAuthentication
#     ]
#     permission_classes = [IsAuthenticated]
#     serializer_class = serializers.ModelSerializer
#     queryset = QuerySet
#
#     def get_queryset(self):
#         queryset = self.queryset.all()
#         query_params = self.request.query_params
#         if isinstance(self.request.data, dict):
#             query_params.update(self.request.data)
#         return queryset.filter(**query_params)
#
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serialized = self.serializer_class(queryset, many=True,  context={'request': request})
#         content = {
#             "totalItems": queryset.count(),
#             "items": serialized.data
#         }
#         return Response(content)

class AbstractListItemView(generics.ListAPIView):
    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ModelSerializer
    queryset = QuerySet

    def get_queryset(self):
        queryset = self.queryset.all()
        query_params = self.request.query_params
        if isinstance(self.request.data, dict):
            query_params.update(self.request.data)
        print(query_params)
        return queryset.filter(**query_params)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized = self.serializer_class(queryset, many=True,  context={'request': request})
        content = {
            "totalItems": queryset.count(),
            "items": serialized.data
        }
        return Response(content)

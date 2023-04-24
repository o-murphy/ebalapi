from django.urls import path
# from drf_yasg.app_settings import swagger_settings
from rest_framework import permissions

from .views import rest as rest

app_name = 'ebalapi_service'

urlpatterns = [

    path('token/', rest.AuthView.as_view()),
    path('auth/', rest.CustomAuthToken.as_view()),

    path('drag_function/', rest.DragFunctionSearchView.as_view(), name='drag_function-search'),
    path('drag_function/<int:pk>/', rest.DragFunctionDetailView.as_view(), name='drag_function-detail'),
    path('drag_functions/', rest.DragFunctionSearchView.as_view()),
    path('drag_functions/<int:pk>/', rest.DragFunctionDetailView.as_view()),

    path('diameter/', rest.DiameterSearchView.as_view(), name='diameter-search'),
    path('diameter/<int:pk>/', rest.DiameterDetailView.as_view(), name='diameter-detail'),
    path('diameters/', rest.DiameterSearchView.as_view()),
    path('diameters/<int:pk>/', rest.DiameterDetailView.as_view()),

    path('caliber/', rest.CaliberSearchView.as_view(), name='caliber-search'),
    path('caliber/<int:pk>/', rest.CaliberDetailView.as_view(), name='caliber-detail'),
    path('calibers/', rest.CaliberSearchView.as_view()),
    path('calibers/<int:pk>/', rest.CaliberDetailView.as_view()),

    path('vendor/', rest.VendorSearchView.as_view(), name='vendor-search'),
    path('vendor/<int:pk>/', rest.VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/', rest.VendorSearchView.as_view()),
    path('vendors/<int:pk>/', rest.VendorDetailView.as_view()),

    path('rifle/', rest.RifleSearchView.as_view(), name='rifle-search'),
    path('rifle/<int:pk>/', rest.RifleDetailView.as_view(), name='rifle-detail'),
    path('rifles/', rest.RifleSearchView.as_view()),
    path('rifles/<int:pk>/', rest.RifleDetailView.as_view()),

    path('bullet/', rest.BulletSearchView.as_view(), name='bullet-search'),
    path('bullet/<int:pk>/', rest.BulletDetailView.as_view(), name='bullet-detail'),
    path('bullets/', rest.BulletSearchView.as_view()),
    path('bullets/<int:pk>/', rest.BulletDetailView.as_view()),

    path('cartridge/', rest.CartridgeSearchView.as_view(), name='cartridge-search'),
    path('cartridge/<int:pk>/', rest.CartridgeDetailView.as_view(), name='cartridge-detail'),
    path('cartridges/', rest.CartridgeSearchView.as_view()),
    path('cartridges/<int:pk>/', rest.CartridgeDetailView.as_view()),

]


# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )
#
# urlpatterns += [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

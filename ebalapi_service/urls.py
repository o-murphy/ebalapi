from django.urls import path

from .views import rest


app_name = 'ebalapi_service'

urlpatterns = [

    path('token/', rest.AuthView.as_view()),
    path('auth/', rest.CustomAuthToken.as_view()),

    path('dragfuncs/', rest.DragFunctionView.as_view(), name='drag_function-search'),
    path('dragfuncs/<int:pk>/', rest.DragFunctionCRUDView.as_view(), name='drag_function-detail'),

    path('diameters/', rest.DiameterSearchView.as_view()),
    path('diameters/<int:pk>/', rest.DiameterDetailView.as_view(), name='diameter-detail'),

    path('calibers/', rest.CaliberSearchView.as_view(), name='caliber-search'),
    path('calibers/<int:pk>/', rest.CaliberDetailView.as_view(), name='caliber-detail'),

    path('vendors/', rest.VendorView.as_view(), name='vendor-search'),
    path('vendors/<int:pk>/', rest.VendorCRUDView.as_view(), name='vendor-detail'),

    path('rifles/', rest.RifleView.as_view(), name='rifle-search'),
    path('rifles/<int:pk>/', rest.RifleCRUDView.as_view(), name='rifle-detail'),

    path('bullets/', rest.BulletSearchView.as_view(), name='bullet-search'),
    path('bullets/<int:pk>/', rest.BulletDetailView.as_view(), name='bullet-detail'),

    path('cartridges/', rest.CartridgeSearchView.as_view(), name='cartridge-search'),
    path('cartridges/<int:pk>/', rest.CartridgeDetailView.as_view(), name='cartridge-detail'),

]

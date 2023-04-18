from django.urls import path

from . import views


app_name = 'ebalapi_service'

urlpatterns = [

    path('token/', views.rest.AuthView.as_view()),
    path('auth/', views.rest.CustomAuthToken.as_view()),

    path('dragfuncs/', views.rest.DragFunctionView.as_view()),
    path('dragfunc/', views.rest.DragFunctionCRUDView.as_view()),
    path('dragfunc/<int:id>/', views.rest.DragFunctionCRUDView.as_view(), name='dragfunction-detail'),

    path('diameters/', views.rest.DiameterView.as_view()),
    path('diameters/<int:id>/', views.rest.DiameterCRUDView.as_view(), name='diameter-detail'),

    path('calibers/', views.rest.CaliberView.as_view(), name='caliber-search'),
    path('calibers/<int:id>/', views.rest.CaliberCRUDView.as_view(), name='caliber-detail'),

    path('vendor/<int:id>/', views.rest.VendorCRUDView.as_view(), name='vendor-detail'),
    path('vendors/', views.rest.VendorView.as_view()),
    path('vendor/', views.rest.VendorCRUDView.as_view()),

    # path('vendor/<int:id>/', views.rest.VendorDetailView.as_view(), name='vendor-detail'),

    path('rifles/', views.rest.RifleView.as_view(), name='rifle-search'),
    # path('rifle/', views.rest.RifleCRUDView.as_view()),
    path('rifles/<int:id>/', views.rest.RifleCRUDView.as_view(), name='rifle-detail'),

    # path('bullets/', views.rest.BulletView.as_view(), name='bullet-search'),
    # path('bullet/', views.rest.BulletCRUDView.as_view()),
    path('bullets/', views.rest.BulletSearchListView.as_view(), name='bullet-search'),
    path('bullets/<int:id>/', views.rest.BulletCRUDView.as_view(), name='bullet-detail'),

    path('cartridges/', views.rest.CartridgeView.as_view(), name='cartridge-search'),
    # path('cartridge/', views.rest.CartridgeCRUDView.as_view()),
    path('cartridges/<int:id>/', views.rest.CartridgeCRUDView.as_view(), name='cartridge-detail'),
    # path('cartridges/', views.rest.CartridgeSearchListView.as_view(), name='cartridge-search'),

]

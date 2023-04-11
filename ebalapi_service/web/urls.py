from django.urls import path

from .. import views


app_name = 'ebalapi_service'

urlpatterns = [

    path('token/', views.rest.AuthView.as_view()),
    path('auth/', views.rest.CustomAuthToken.as_view()),

    path('dragfuncs/', views.rest.DragFunctionView.as_view()),
    path('dragfunc/', views.rest.DragFunctionCRUDView.as_view()),

    path('diameters/', views.rest.DiameterView.as_view()),
    # path('diameter/', views.rest.DiameterCRUDView.as_view()),

    path('calibers/', views.rest.CaliberView.as_view(), name='caliber-list'),
    path('caliber/', views.rest.CaliberCRUDView.as_view(), name='caliber-detail'),
    path('caliber/<int:id>/', views.rest.CaliberDetailView.as_view(), name='caliber-detail'),

    path('vendors/', views.rest.VendorView.as_view()),
    path('vendor/', views.rest.VendorCRUDView.as_view()),
    path('vendor/<int:id>/', views.rest.VendorDetailView.as_view(), name='vendor-detail'),

    path('rifles/', views.rest.RifleView.as_view()),
    path('rifle/', views.rest.RifleCRUDView.as_view()),

    path('bullets/', views.rest.BulletView.as_view()),
    path('bullet/', views.rest.BulletCRUDView.as_view()),

    path('cartridges/', views.rest.CartridgeView.as_view()),
    path('cartridge/', views.rest.CartridgeCRUDView.as_view()),

]

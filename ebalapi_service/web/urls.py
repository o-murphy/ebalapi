from django.urls import path

from .. import views


app_name = 'ebalapi_service'

urlpatterns = [

    path('token/', views.rest.AuthView.as_view()),
    path('auth/', views.rest.CustomAuthToken.as_view()),

    path('drag_functions/', views.rest.DragFunctionView.as_view()),
    path('drag_function/', views.rest.DragFunctionCRUDView.as_view()),

    path('diameters/', views.rest.DiameterView.as_view()),
    # path('diameter/', views.rest.DiameterCRUDView.as_view()),

    path('calibers/', views.rest.CaliberView.as_view()),
    path('caliber/', views.rest.CaliberCRUDView.as_view()),

    path('vendors/', views.rest.VendorView.as_view()),
    path('vendor/', views.rest.VendorCRUDView.as_view()),

    #
    # path('bullets/', views.rest.BulletView.as_view()),
    # path('bullet/', views.rest.BulletCRUDView.as_view()),

]

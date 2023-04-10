from django.urls import path

from .. import views


app_name = 'ebalapi_service'

urlpatterns = [

    path('token/', views.rest.AuthView.as_view()),
    path('auth/', views.rest.CustomAuthToken.as_view()),

    path('calibers/', views.rest.CaliberView.as_view()),
    path('caliber/', views.rest.CaliberCRUDView.as_view()),

    path('bullets/', views.rest.BulletView.as_view()),
    path('bullet/', views.rest.BulletCRUDView.as_view()),

]

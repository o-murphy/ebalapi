"""
URL configuration for ebalapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

from ebalapi_service.web import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('ebalapi/', include(('ebalapi_service.web.urls', 'ebalapi_service'), namespace='ebalapi_service')),
]

urlpatterns += [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [

    path('api/token/', views.rest_api.AuthView.as_view()),
    path('api/auth/', views.rest_api.CustomAuthToken.as_view()),

    path('api/calibers/', views.rest_api.CaliberView.as_view()),

    path('api/caliber_inst/', views.rest_api.CaliberCRUDView.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)
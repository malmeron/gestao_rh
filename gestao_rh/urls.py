"""gestao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from rest_framework import routers
from core import views

from funcionarios.api.views import FuncionarioViewSet
from registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/banco-horas', RegistroHoraExtraViewSet)


urlpatterns = [
    path('', include('core.urls')), #quando não digitar nada levar para core
    path('funcionarios/', include('funcionarios.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('empresas/', include('empresas.urls')),
    path('documentos/', include('documentos.urls')),
    path('horas-extras/', include('registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),



    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

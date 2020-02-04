"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# import rest_framework
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from apps.stalls.views import StallViewSet
from apps.manifests.views import ManifestViewSet, ManifestInfoViewSet
from apps.cargos.views import CargoViewSet, CargoTypeViewSet, CargoBoxTypeViewSet
from apps.customers.views import CustomerViewSet, CustomerLabelViewSet
from apps.storages.views import StorageViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'manifestinfo', ManifestInfoViewSet)
router.register(r'manifest', ManifestViewSet)
router.register(r'cargo', CargoViewSet)
router.register(r'cargotype', CargoTypeViewSet)
router.register(r'cargoboxtype', CargoBoxTypeViewSet)
router.register(r'stall', StallViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'customerlabel', CustomerLabelViewSet)
router.register(r'storage', StorageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title="API文档")),
    # path('api-auth/', include("rest_framework.urls")),
    path('api/', include(router.urls))
]

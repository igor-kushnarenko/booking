from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from board import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'seats', views.SeatsViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'vault', views.VaultViewSet)
router.register(r'rate', views.RateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

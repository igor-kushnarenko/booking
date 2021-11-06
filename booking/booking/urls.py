from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from board.views import UserViewSet, BookingViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('router/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

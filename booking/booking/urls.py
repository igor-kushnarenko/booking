from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from board import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'booking', views.BookingViewSet)
router.register(r'rate', views.RateViewSet)
router.register(r'service', views.ServiceViewSet)
# router.register(r'price_rate', views.PriceRateViewSet)
router.register(r'time', views.TimeViewSet)
router.register(r'chair', views.ChairViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('router/', include(router.urls)),
]

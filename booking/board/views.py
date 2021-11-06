from rest_framework import viewsets, permissions

from board import serializers
from board import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class PriceRateViewSet(viewsets.ModelViewSet):
    queryset = models.PriceRate.objects.all()
    serializer_class = serializers.PriceRateSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


class ChairViewSet(viewsets.ModelViewSet):
    queryset = models.Chair.objects.all()
    serializer_class = serializers.ChairSerializer

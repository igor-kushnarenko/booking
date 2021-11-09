from rest_framework import viewsets

from board import serializers
from board import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDevicesViewSet(viewsets.ModelViewSet):
    queryset = models.UserDevices.objects.all()
    serializer_class = serializers.UserDevicesSerializer


class SeatsViewSet(viewsets.ModelViewSet):
    queryset = models.Seats.objects.all()
    serializer_class = serializers.SeatsSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class VaultViewSet(viewsets.ModelViewSet):
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer

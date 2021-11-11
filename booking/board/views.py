from rest_framework import viewsets
from rest_framework import generics

from board import serializers
from board import models


class UserListView(generics.ListAPIView):
    # queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        queryset = models.User.objects.all()
        params = self.request.query_params
        # фильтры для поиска через запрос: http://127.0.0.1:8000/api/user/all?id=1
        id = params.get('id', None)
        first_name = params.get('first_name', None)
        second_name = params.get('second_name', None)
        email = params.get('email', None)

        if id:
            queryset = queryset.filter(id=id)
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        if second_name:
            queryset = queryset.filter(second_name=second_name)
        if email:
            queryset = queryset.filter(email=email)

        return queryset


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDestroyView(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ServiceListView(generics.ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceCreateView(generics.CreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class UserDevicesViewSet(viewsets.ModelViewSet):
    queryset = models.UserDevices.objects.all()
    serializer_class = serializers.UserDevicesSerializer


class SeatsViewSet(viewsets.ModelViewSet):
    queryset = models.Seats.objects.all()
    serializer_class = serializers.SeatsSerializer


class VaultViewSet(viewsets.ModelViewSet):
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer

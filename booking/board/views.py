from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from board import serializers
from board import models


class UserListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserUpdateView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDestroyView(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ServiceListView(generics.ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class ServiceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceCreateView(generics.CreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class RateListViewSet(generics.ListAPIView):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer
    permission_classes = [permissions.IsAuthenticated]


class RateRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer
    permission_classes = [permissions.IsAdminUser]


class RateUpdateView(generics.UpdateAPIView):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer
    permission_classes = [permissions.IsAdminUser]


class RateCreateView(generics.CreateAPIView):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer
    permission_classes = [permissions.IsAdminUser]


class VisitListView(generics.ListAPIView):
    queryset = models.Visit.objects.all()
    serializer_class = serializers.VisitSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDevicesViewSet(viewsets.ModelViewSet):
    queryset = models.UserDevices.objects.all()
    serializer_class = serializers.UserDevicesSerializer
    permission_classes = [permissions.IsAdminUser]


class SeatsViewSet(viewsets.ModelViewSet):
    queryset = models.Seats.objects.all()
    serializer_class = serializers.SeatsSerializer
    permission_classes = [permissions.IsAuthenticated]


class VaultViewSet(viewsets.ModelViewSet):
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer
    permission_classes = [permissions.IsAuthenticated]


class TimeViewSet(viewsets.ModelViewSet):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RateViewSet(viewsets.ModelViewSet):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer
    permission_classes = [permissions.IsAuthenticated]

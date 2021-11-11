from rest_framework import serializers
from board import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserDevicesSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user')

    class Meta:
        model = models.UserDevices
        fields = ['device_firebase_id', 'uuid', 'jwt', 'jwt_renew', 'user_name']


class SeatsSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service')

    class Meta:
        model = models.Seats
        fields = ('service_name', 'seat_number')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class VaultSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service')

    class Meta:
        model = models.Vault
        fields = ('service_name', 'vault_number')


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vault
        fields = ('time',)


class RateSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service')

    class Meta:
        model = models.Rate
        fields = ('name', 'price', 'description', 'service_name')

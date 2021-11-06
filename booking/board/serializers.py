from rest_framework import serializers
from board.models import User, Booking


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'email']


class BookingSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user')
    service_name = serializers.CharField(source='service')
    date_name = serializers.CharField(source='date')
    time_name = serializers.CharField(source='time')
    chair_name = serializers.CharField(source='chair')
    rate_name = serializers.CharField(source='rate')

    class Meta:
        model = Booking
        fields = ('id', 'user_name', 'service_name', 'date_name', 'time_name', 'chair_name', 'rate_name')

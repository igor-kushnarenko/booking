from django.contrib import admin

from board.models import User, Service, Rate, Chair, Time, Booking


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'email']
    list_display_links = ['second_name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Chair)
class ChairAdmin(admin.ModelAdmin):
    list_display = ['service', 'number']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'date', 'time', 'chair', 'rate']


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['start_time']

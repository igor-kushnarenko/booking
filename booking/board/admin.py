from django.contrib import admin

from board import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['second_name', 'first_name', 'email']
    list_display_links = ['second_name']


@admin.register(models.Auth)
class AuthAdmin(admin.ModelAdmin):
    list_display = ['user', 'login', 'password']


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ['service', 'seat_number']


@admin.register(models.Vault)
class VaultAdmin(admin.ModelAdmin):
    list_display = ['service', 'vault_number']


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['date_visit', 'time', 'service', 'user']


@admin.register(models.Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['start_time']


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['visit', 'reservation', 'ticket_number', 'number_persons', 'rate']


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation_date']


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'rate']


@admin.register(models.Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'service']

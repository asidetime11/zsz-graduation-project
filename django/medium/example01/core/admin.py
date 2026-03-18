from django.contrib import admin

from .models import Order, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone", "id_card", "passport_no")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "items", "total_price", "address", "payment_card", "status", "passport_no")

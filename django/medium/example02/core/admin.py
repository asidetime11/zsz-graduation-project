from django.contrib import admin

from .models import PaymentInfo, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone")


@admin.register(PaymentInfo)
class PaymentInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "card_number", "cvv", "expiry_date", "api_token", "bank_name")

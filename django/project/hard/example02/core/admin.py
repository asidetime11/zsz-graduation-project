from django.contrib import admin

from .models import APIIntegration, Transaction, UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone", "ssn", "bank_account", "card_number", "cvv")


@admin.register(APIIntegration)
class APIIntegrationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "service_name", "api_key", "api_secret", "webhook_secret", "private_key")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "from_account", "to_account", "amount", "card_number", "status", "created_at")

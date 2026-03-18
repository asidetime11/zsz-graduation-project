from django.contrib import admin

from .models import Organization, PaymentCard, Report


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "api_key", "webhook_secret")


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "organization", "title", "created_by", "created_at")


@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    list_display = ("id", "organization", "card_number", "cvv", "expiry_date")

from django.contrib import admin

from .models import ExportTask, Notification, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "id_card", "phone", "card_number", "cvv")


@admin.register(ExportTask)
class ExportTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "file_path", "task_payload", "created_at")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message", "sent_at")

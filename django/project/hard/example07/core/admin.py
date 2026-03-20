from django.contrib import admin

from .models import AuditLog, BackupRecord, Transaction, UserAccount

admin.site.register(UserAccount)
admin.site.register(Transaction)
admin.site.register(AuditLog)
admin.site.register(BackupRecord)

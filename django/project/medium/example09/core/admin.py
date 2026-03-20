from django.contrib import admin

from .models import LoginAudit, UserAccount

admin.site.register(UserAccount)
admin.site.register(LoginAudit)

from django.contrib import admin

from .models import AccessLog, Department, Document, Organization

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Document)
admin.site.register(AccessLog)

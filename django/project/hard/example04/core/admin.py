from django.contrib import admin

from .models import CacheRecord, Organization, UserProfile

admin.site.register(Organization)
admin.site.register(UserProfile)
admin.site.register(CacheRecord)

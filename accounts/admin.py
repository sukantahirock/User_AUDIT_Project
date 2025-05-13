from django.contrib import admin
from .models import CustomUser, UserProfile, AuditLog
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(AuditLog)
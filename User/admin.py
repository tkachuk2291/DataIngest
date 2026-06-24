from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from User.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'role')
    list_filter = ('role',)
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
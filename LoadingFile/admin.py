from django.contrib import admin

from LoadingFile.models import LoadFile


@admin.register(LoadFile)
class LoadFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'user_email', 'create_date', 'loading_status', 'error')
    list_filter = ('loading_status',)
    readonly_fields = ('file_name', 'file_hash', 'create_date', 'loading_status', 'error', 'user')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
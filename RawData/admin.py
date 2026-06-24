from django.contrib import admin

from .models import RawData


@admin.register(RawData)
class RawDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'advertiser', 'brand', 'start', 'end', 'format', 'platform', 'impr')
    list_select_related = ('file__user',)
    list_filter = ('file__user',)

    @admin.display(description='User')
    def get_user(self, obj):
        return obj.file.user

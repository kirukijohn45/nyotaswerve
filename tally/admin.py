from django.contrib import admin
from .models import TallySyncLog

@admin.register(TallySyncLog)
class TallySyncLogAdmin(admin.ModelAdmin):
    list_display = ('direction', 'entity_type', 'status', 'created_at')
    list_filter = ('direction', 'entity_type', 'status')
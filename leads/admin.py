from django.contrib import admin
from .models import Lead, LeadSource


@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'is_active')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'estimated_value', 'assigned_to', 'created_at')
    list_filter = ('status', 'priority', 'source')
    search_fields = ('title', 'contact__first_name', 'contact__last_name')
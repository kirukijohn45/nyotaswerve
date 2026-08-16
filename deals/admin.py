from django.contrib import admin
from .models import Pipeline, PipelineStage, Deal


@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')


@admin.register(PipelineStage)
class PipelineStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'pipeline', 'order', 'color', 'probability')


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'pipeline', 'stage', 'amount', 'assigned_to', 'priority', 'is_active')
    list_filter = ('pipeline', 'stage', 'priority', 'is_won')
    search_fields = ('title', 'contact__first_name', 'contact__last_name')
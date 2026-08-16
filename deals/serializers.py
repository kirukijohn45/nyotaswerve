from rest_framework import serializers
from .models import Pipeline, PipelineStage, Deal


class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipeline
        fields = '__all__'


class PipelineStageSerializer(serializers.ModelSerializer):
    deal_count = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()
    
    class Meta:
        model = PipelineStage
        fields = '__all__'
    
    def get_deal_count(self, obj):
        return obj.deals.filter(is_active=True).count()
    
    def get_total_amount(self, obj):
        from django.db.models import Sum
        return obj.deals.filter(is_active=True).aggregate(
            total=Sum('amount')
        )['total'] or 0


class DealSerializer(serializers.ModelSerializer):
    contact_name = serializers.ReadOnlyField(source='contact.full_name', default='')
    company_name = serializers.ReadOnlyField(source='company.name', default='')
    stage_name = serializers.ReadOnlyField(source='stage.name', default='')
    stage_color = serializers.ReadOnlyField(source='stage.color', default='#6B7280')
    
    class Meta:
        model = Deal
        fields = '__all__'
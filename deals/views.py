from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets
from .models import Pipeline, PipelineStage, Deal
from .serializers import PipelineSerializer, PipelineStageSerializer, DealSerializer


class PipelineViewSet(viewsets.ModelViewSet):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer


class PipelineStageViewSet(viewsets.ModelViewSet):
    queryset = PipelineStage.objects.all()
    serializer_class = PipelineStageSerializer


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    filterset_fields = ['pipeline', 'stage', 'assigned_to', 'priority', 'is_won']
    search_fields = ['title', 'contact__first_name', 'contact__last_name', 'company__name']


@login_required
def kanban_board(request, pipeline_id=None):
    """Kanban board view - the main deal management UI."""
    pipelines = Pipeline.objects.filter(is_active=True)
    active_pipeline = get_object_or_404(Pipeline, pk=pipeline_id) if pipeline_id else pipelines.first()
    
    if active_pipeline:
        stages = active_pipeline.stages.all()
        deals = Deal.objects.filter(pipeline=active_pipeline, is_active=True).select_related(
            'contact', 'company', 'assigned_to', 'stage'
        )
        deals_by_stage = {stage.id: deals.filter(stage=stage) for stage in stages}
    else:
        stages = []
        deals_by_stage = {}
    
    return render(request, 'deals/kanban.html', {
        'pipelines': pipelines,
        'active_pipeline': active_pipeline,
        'stages': stages,
        'deals_by_stage': deals_by_stage,
    })


@login_required
def deal_list(request):
    deals = Deal.objects.all().select_related('pipeline', 'stage', 'contact', 'assigned_to')
    return render(request, 'deals/list.html', {'deals': deals})


@login_required
def deal_detail(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    return render(request, 'deals/detail.html', {'deal': deal})


@login_required
@require_POST
@csrf_exempt
def update_deal_stage(request, pk):
    """API endpoint to update deal stage (for drag-and-drop)."""
    try:
        data = json.loads(request.body)
        deal = get_object_or_404(Deal, pk=pk)
        stage_id = data.get('stage_id')
        order = data.get('order', 0)
        
        stage = get_object_or_404(PipelineStage, pk=stage_id)
        deal.stage = stage
        deal.order = order
        deal.save()
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Lead, LeadSource
from .serializers import LeadSerializer, LeadSourceSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filterset_fields = ['status', 'priority', 'assigned_to', 'source']
    search_fields = ['title', 'description', 'contact__first_name', 'contact__last_name']


class LeadSourceViewSet(viewsets.ModelViewSet):
    queryset = LeadSource.objects.all()
    serializer_class = LeadSourceSerializer


@login_required
def lead_list(request):
    leads = Lead.objects.all().select_related('contact', 'assigned_to', 'source')
    return render(request, 'leads/list.html', {'leads': leads})


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/detail.html', {'lead': lead})
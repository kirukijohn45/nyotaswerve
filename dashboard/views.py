from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from deals.models import Deal, PipelineStage
from leads.models import Lead
from contacts.models import Contact
from invoices.models import Invoice
from tasks.models import Task


@login_required
def home(request):
    """Main dashboard after login."""
    
    # Summary stats
    total_deals = Deal.objects.filter(is_active=True).count()
    total_leads = Lead.objects.filter(is_active=True).count()
    total_contacts = Contact.objects.filter(is_active=True).count()
    
    # Pipeline value
    pipeline_value = Deal.objects.filter(
        is_active=True, is_won__isnull=True
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Won deals this month
    month_start = timezone.now().replace(day=1)
    won_this_month = Deal.objects.filter(
        is_won=True, closed_date__gte=month_start
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Deals by stage
    stages = PipelineStage.objects.all().annotate(
        deal_count=Count('deals', filter=Q(deals__is_active=True))
    )
    
    # Recent deals
    recent_deals = Deal.objects.filter(is_active=True).select_related(
        'stage', 'contact', 'assigned_to'
    ).order_by('-created_at')[:10]
    
    # Recent leads
    recent_leads = Lead.objects.filter(is_active=True).select_related(
        'contact', 'assigned_to'
    ).order_by('-created_at')[:10]
    
    # Upcoming tasks
    upcoming_tasks = Task.objects.filter(
        status__in=['pending', 'in_progress'],
        due_date__isnull=False
    ).select_related('assigned_to').order_by('due_date')[:10]
    
    # Recent invoices
    recent_invoices = Invoice.objects.all().select_related(
        'contact', 'company'
    ).order_by('-created_at')[:10]
    
    # Overdue invoices
    overdue_invoices = Invoice.objects.filter(
        status='overdue'
    ).count()
    
    context = {
        'total_deals': total_deals,
        'total_leads': total_leads,
        'total_contacts': total_contacts,
        'pipeline_value': pipeline_value,
        'won_this_month': won_this_month,
        'stages': stages,
        'recent_deals': recent_deals,
        'recent_leads': recent_leads,
        'upcoming_tasks': upcoming_tasks,
        'recent_invoices': recent_invoices,
        'overdue_invoices': overdue_invoices,
    }
    return render(request, 'dashboard/home.html', context)
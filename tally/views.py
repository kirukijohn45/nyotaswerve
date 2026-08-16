from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .tally_client import TallyClient
from .models import TallySyncLog


@staff_member_required
def tally_dashboard(request):
    """Tally integration dashboard view."""
    logs = TallySyncLog.objects.all()[:50]
    return render(request, 'tally/dashboard.html', {'logs': logs})


@staff_member_required
def test_tally_connection(request):
    """Test connection to Tally Prime."""
    client = TallyClient()
    success, message = client.test_connection()
    return JsonResponse({'success': success, 'message': message})


@staff_member_required
def sync_ledgers(request):
    """Sync ledgers from Tally Prime."""
    try:
        client = TallyClient()
        response = client.get_ledgers()
        
        TallySyncLog.objects.create(
            direction='import',
            entity_type='ledger',
            status='success',
            response_xml=response[:1000],
        )
        return JsonResponse({'success': True, 'message': 'Ledgers fetched successfully'})
    except Exception as e:
        TallySyncLog.objects.create(
            direction='import',
            entity_type='ledger',
            status='failed',
            error_message=str(e),
        )
        return JsonResponse({'success': False, 'message': str(e)})
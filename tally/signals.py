"""
Signals for automatic Tally Prime synchronization.
When invoices are paid or created, auto-sync to Tally.
"""
import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

logger = logging.getLogger(__name__)


def should_auto_sync():
    """Check if auto-sync is enabled."""
    return getattr(settings, 'TALLY_AUTO_SYNC', True)


@receiver(post_save, sender='invoices.Invoice')
def auto_sync_invoice_to_tally(sender, instance, created, **kwargs):
    """
    Auto-sync invoice to Tally Prime when status changes to 'sent' or 'paid'.
    """
    if not should_auto_sync():
        return
    
    # Only sync if status is sent or paid and not already synced
    if instance.status in ('sent', 'paid') and not instance.tally_synced:
        try:
            from .tally_client import TallyClient
            from .models import TallySyncLog
            
            client = TallyClient()
            
            # Build items for Tally voucher
            items = []
            for line in instance.lines.all():
                items.append({
                    'stock_name': line.product.name if line.product else line.description,
                    'quantity': float(line.quantity),
                    'rate': float(line.unit_price),
                    'amount': float(line.line_total),
                })
            
            # Create sales voucher in Tally
            party_name = None
            if instance.contact:
                party_name = instance.contact.full_name
            elif instance.company:
                party_name = instance.company.name
            
            if party_name:
                response = client.create_sales_voucher(
                    voucher_no=instance.invoice_number,
                    date=instance.issue_date.isoformat(),
                    party_ledger_name=party_name,
                    items=items,
                    amount=float(instance.total),
                    currency=instance.currency,
                )
                
                # Mark as synced
                instance.tally_synced = True
                instance.tally_voucher_no = instance.invoice_number
                instance.save(update_fields=['tally_synced', 'tally_voucher_no'])
                
                TallySyncLog.objects.create(
                    direction='export',
                    entity_type='invoice',
                    entity_id=str(instance.id),
                    status='success',
                    tally_ledger_name=party_name,
                    tally_voucher_no=instance.invoice_number,
                )
        except Exception as e:
            from .models import TallySyncLog
            TallySyncLog.objects.create(
                direction='export',
                entity_type='invoice',
                entity_id=str(instance.id),
                status='failed',
                error_message=str(e),
            )
            logger.error(f'Failed to auto-sync invoice {instance.invoice_number} to Tally: {e}')


@receiver(post_save, sender='contacts.Contact')
def auto_sync_contact_to_tally(sender, instance, created, **kwargs):
    """
    Auto-sync new contacts as ledgers in Tally.
    """
    if not should_auto_sync():
        return
    
    if not created:
        return
    
    try:
        from .tally_client import TallyClient
        from .models import TallySyncLog
        
        client = TallyClient()
        response = client.create_ledger(
            name=instance.full_name,
            mailing_name=instance.full_name,
            address=instance.address,
            city=instance.city,
            state=instance.state,
            pincode=instance.postal_code,
            phone=instance.phone or instance.mobile,
            email=instance.email,
        )
        
        TallySyncLog.objects.create(
            direction='export',
            entity_type='contact',
            entity_id=str(instance.id),
            status='success',
            tally_ledger_name=instance.full_name,
        )
    except Exception as e:
        from .models import TallySyncLog
        TallySyncLog.objects.create(
            direction='export',
            entity_type='contact',
            entity_id=str(instance.id),
            status='failed',
            error_message=str(e),
        )
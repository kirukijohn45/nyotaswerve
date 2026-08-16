from django.db import models


class TallySyncLog(models.Model):
    """Log of Tally Prime sync operations."""
    
    DIRECTION_CHOICES = [
        ('import', 'Import from Tally'),
        ('export', 'Export to Tally'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    
    ENTITY_CHOICES = [
        ('ledger', 'Ledger'),
        ('voucher', 'Voucher'),
        ('stock_item', 'Stock Item'),
        ('contact', 'Contact'),
        ('invoice', 'Invoice'),
    ]
    
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    entity_type = models.CharField(max_length=20, choices=ENTITY_CHOICES)
    entity_id = models.CharField(max_length=100, blank=True, default='', help_text='ID of the synced entity')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    request_xml = models.TextField(blank=True, default='')
    response_xml = models.TextField(blank=True, default='')
    
    error_message = models.TextField(blank=True, default='')
    tally_ledger_name = models.CharField(max_length=200, blank=True, default='')
    tally_voucher_no = models.CharField(max_length=100, blank=True, default='')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tally_sync_logs'
        verbose_name = 'Tally Sync Log'
        verbose_name_plural = 'Tally Sync Logs'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.direction} {self.entity_type} - {self.status}'
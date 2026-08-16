from django.db import models
from django.conf import settings


class LeadSource(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#6B7280')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'crm_lead_sources'
    
    def __str__(self):
        return self.name


class Lead(models.Model):
    """Potential sales lead."""
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('proposal', 'Proposal'),
        ('negotiation', 'Negotiation'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, default='')
    
    contact = models.ForeignKey(
        'contacts.Contact', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='leads'
    )
    company = models.ForeignKey(
        'contacts.Company', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='leads'
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    source = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, null=True, blank=True)
    
    estimated_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    probability = models.IntegerField(default=0, help_text='Win probability (0-100%)')
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='leads_created'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='leads_assigned'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_close_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'crm_leads'
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
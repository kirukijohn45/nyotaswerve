from django.db import models
from django.conf import settings


class Pipeline(models.Model):
    """Sales pipeline (e.g., Sales, Recruitment)."""
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'crm_pipelines'
        ordering = ['order']
    
    def __str__(self):
        return self.name


class PipelineStage(models.Model):
    """Stage within a pipeline (e.g., New, Contacted, Qualified)."""
    
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, related_name='stages')
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7, default='#6B7280')
    order = models.IntegerField(default=0)
    probability = models.IntegerField(default=0, help_text='Default win probability')
    
    class Meta:
        db_table = 'crm_pipeline_stages'
        ordering = ['pipeline', 'order']
    
    def __str__(self):
        return f'{self.pipeline.name} - {self.name}'


class Deal(models.Model):
    """Sales deal/opportunity - the core of the kanban board."""
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, default='')
    
    pipeline = models.ForeignKey(Pipeline, on_delete=models.PROTECT, related_name='deals')
    stage = models.ForeignKey(PipelineStage, on_delete=models.PROTECT, related_name='deals')
    
    contact = models.ForeignKey(
        'contacts.Contact', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='deals'
    )
    company = models.ForeignKey(
        'contacts.Company', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='deals'
    )
    
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, default='KES')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    probability = models.IntegerField(default=0, help_text='Win probability (0-100%)')
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='deals_created'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='deals_assigned'
    )
    
    order = models.IntegerField(default=0, help_text='Order within stage')
    
    expected_close_date = models.DateField(null=True, blank=True)
    closed_date = models.DateField(null=True, blank=True)
    is_won = models.BooleanField(null=True, default=None)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'crm_deals'
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'
        ordering = ['stage__pipeline', 'stage__order', 'order']
    
    def __str__(self):
        return self.title
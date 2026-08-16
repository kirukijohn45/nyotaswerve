from django.db import models


class Category(models.Model):
    """Product/Service category."""
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'crm_product_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Product or service offered."""
    
    TYPE_CHOICES = [
        ('product', 'Product'),
        ('service', 'Service'),
    ]
    
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, default='')
    sku = models.CharField(max_length=100, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='product')
    
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.CharField(max_length=50, blank=True, default='pcs', help_text='e.g., pcs, hours, kg')
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text='Tax %')
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'crm_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
from django.contrib import admin
from .models import Contact, Company


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'contact_type', 'company', 'is_active')
    list_filter = ('contact_type', 'is_active', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'industry', 'is_active')
    list_filter = ('industry', 'is_active')
    search_fields = ('name', 'email')
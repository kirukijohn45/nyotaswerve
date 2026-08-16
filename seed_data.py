"""
Seed script to populate the CRM with demo data.
Run: python seed_data.py
"""
import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.utils import timezone
from datetime import timedelta, date
from accounts.models import User
from contacts.models import Contact, Company
from leads.models import Lead, LeadSource
from deals.models import Pipeline, PipelineStage, Deal
from tasks.models import Task
from products.models import Product, Category
from invoices.models import Invoice, InvoiceLine

def seed():
    admin = User.objects.get(username='admin')
    
    # --- Pipeline & Stages ---
    pipeline, _ = Pipeline.objects.get_or_create(name='Sales Pipeline', defaults={'order': 0})
    
    stages_data = [
        ('New Lead', '#3B82F6', 0, 10),
        ('Contacted', '#8B5CF6', 1, 20),
        ('Qualified', '#F59E0B', 2, 40),
        ('Proposal', '#EC4899', 3, 60),
        ('Negotiation', '#EF4444', 4, 80),
        ('Closed Won', '#10B981', 5, 100),
        ('Closed Lost', '#6B7280', 6, 0),
    ]
    
    stages = {}
    for name, color, order, prob in stages_data:
        stage, _ = PipelineStage.objects.get_or_create(
            pipeline=pipeline,
            name=name,
            defaults={'color': color, 'order': order, 'probability': prob}
        )
        stages[name] = stage
    
    # --- Lead Sources ---
    sources_data = [
        ('Website', '#3B82F6'),
        ('Referral', '#10B981'),
        ('Social Media', '#8B5CF6'),
        ('Phone Inquiry', '#F59E0B'),
        ('Walk-in', '#EC4899'),
    ]
    for name, color in sources_data:
        LeadSource.objects.get_or_create(name=name, defaults={'color': color})
    
    # --- Product Categories & Products ---
    cat, _ = Category.objects.get_or_create(name='Software', defaults={'description': 'Software products and licenses'})
    Product.objects.get_or_create(
        name='CRM Premium License',
        defaults={
            'sku': 'CRM-PRM-001',
            'category': cat,
            'product_type': 'service',
            'unit_price': 25000,
            'unit': 'year',
            'tax_rate': 16,
        }
    )
    Product.objects.get_or_create(
        name='Tally Integration Module',
        defaults={
            'sku': 'TALLY-INT-001',
            'category': cat,
            'product_type': 'service',
            'unit_price': 45000,
            'unit': 'once',
            'tax_rate': 16,
        }
    )
    
    cat2, _ = Category.objects.get_or_create(name='Consulting', defaults={'description': 'Consulting services'})
    Product.objects.get_or_create(
        name='Business Consultation',
        defaults={
            'sku': 'CONS-001',
            'category': cat2,
            'product_type': 'service',
            'unit_price': 15000,
            'unit': 'hour',
            'tax_rate': 16,
        }
    )
    
    # --- Contacts & Companies ---
    companies_data = [
        ('TechVentures Ltd', 'info@techventures.co.ke', 'Nairobi', 'Technology'),
        ('Safari Logistics', 'contact@safari-logistics.com', 'Mombasa', 'Logistics'),
        ('Green Valley Farms', 'info@greenvalley.co.ke', 'Nakuru', 'Agriculture'),
        ('Blue Ridge Properties', 'sales@blueridge.co.ke', 'Nairobi', 'Real Estate'),
    ]
    
    contacts_data = [
        ('John', 'Mwangi', 'john@techventures.co.ke', '+254712345678', 'TechVentures Ltd'),
        ('Sarah', 'Wanjiku', 'sarah@safari-logistics.com', '+254723456789', 'Safari Logistics'),
        ('Peter', 'Kamau', 'peter@greenvalley.co.ke', '+254734567890', 'Green Valley Farms'),
        ('Grace', 'Nyambura', 'grace@blueridge.co.ke', '+254745678901', 'Blue Ridge Properties'),
        ('David', 'Ochieng', 'david@email.com', '+254756789012', ''),
        ('Mary', 'Akinyi', 'mary@email.com', '+254767890123', ''),
    ]
    
    for name, email, city, industry in companies_data:
        Company.objects.get_or_create(
            name=name,
            defaults={
                'email': email,
                'city': city,
                'industry': industry,
                'created_by': admin,
            }
        )
    
    for first, last, email, phone, company_name in contacts_data:
        contact, _ = Contact.objects.get_or_create(
            first_name=first,
            last_name=last,
            defaults={
                'email': email,
                'phone': phone,
                'company': company_name,
                'created_by': admin,
                'assigned_to': admin,
                'contact_type': 'lead',
            }
        )
    
    # --- Deals ---
    deals_data = [
        ('CRM Software Implementation', stages['New Lead'], 'John Mwangi', 450000, 'high', 'TechVentures Ltd'),
        ('Logistics Management System', stages['Contacted'], 'Sarah Wanjiku', 680000, 'urgent', 'Safari Logistics'),
        ('Farm IoT Sensors', stages['Qualified'], 'Peter Kamau', 320000, 'medium', 'Green Valley Farms'),
        ('Property Management Portal', stages['Proposal'], 'Grace Nyambura', 890000, 'high', 'Blue Ridge Properties'),
        ('Cloud Migration Project', stages['Negotiation'], 'David Ochieng', 1200000, 'urgent', ''),
        ('Website Redesign', stages['New Lead'], 'Mary Akinyi', 180000, 'low', ''),
        ('ERP Integration', stages['Contacted'], 'John Mwangi', 560000, 'medium', 'TechVentures Ltd'),
        ('Data Analytics Dashboard', stages['Qualified'], 'Sarah Wanjiku', 420000, 'high', 'Safari Logistics'),
    ]
    
    for title, stage, contact_name, amount, priority, company_name in deals_data:
        try:
            contact = Contact.objects.filter(
                first_name=contact_name.split()[0],
                last_name=contact_name.split()[1]
            ).first()
            company = Company.objects.filter(name=company_name).first() if company_name else None
            
            Deal.objects.get_or_create(
                title=title,
                defaults={
                    'pipeline': pipeline,
                    'stage': stage,
                    'contact': contact,
                    'company': company,
                    'amount': amount,
                    'priority': priority,
                    'probability': stage.probability,
                    'assigned_to': admin,
                    'created_by': admin,
                    'expected_close_date': date.today() + timedelta(days=30),
                }
            )
        except Exception as e:
            print(f"  Skipping deal '{title}': {e}")
    
    # --- Tasks ---
    task_titles = [
        ('Call John about CRM demo', 'call', 'high', 'John'),
        ('Send proposal to Sarah', 'email', 'medium', 'Sarah'),
        ('Prepare IoT presentation', 'meeting', 'high', 'Peter'),
        ('Follow up on property portal', 'follow_up', 'urgent', 'Grace'),
    ]
    
    for title, task_type, priority, name in task_titles:
        contact = Contact.objects.filter(first_name=name).first()
        Task.objects.get_or_create(
            title=title,
            defaults={
                'task_type': task_type,
                'priority': priority,
                'status': 'pending',
                'assigned_to': admin,
                'created_by': admin,
                'due_date': timezone.now() + timedelta(days=2),
            }
        )
    
    print('✅ Seed data created successfully!')
    print(f'   Users: 1')
    print(f'   Pipelines: 1')
    print(f'   Pipeline Stages: {PipelineStage.objects.count()}')
    print(f'   Companies: {Company.objects.count()}')
    print(f'   Contacts: {Contact.objects.count()}')
    print(f'   Deals: {Deal.objects.count()}')
    print(f'   Lead Sources: {LeadSource.objects.count()}')
    print(f'   Products: {Product.objects.count()}')
    print(f'   Tasks: {Task.objects.count()}')

if __name__ == '__main__':
    seed()
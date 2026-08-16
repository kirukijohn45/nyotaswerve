from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .models import Contact, Company
from .serializers import ContactSerializer, CompanySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_fields = ['contact_type', 'assigned_to', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'company']


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_fields = ['industry', 'is_active']
    search_fields = ['name', 'email', 'phone']


@login_required
def contact_list(request):
    contacts = Contact.objects.all().select_related('assigned_to')
    return render(request, 'contacts/list.html', {'contacts': contacts})


@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/detail.html', {'contact': contact})
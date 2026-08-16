from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Invoice, InvoiceLine
from .serializers import InvoiceSerializer, InvoiceLineSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filterset_fields = ['status', 'contact', 'company']
    search_fields = ['invoice_number', 'contact__first_name', 'contact__last_name']


class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.all()
    serializer_class = InvoiceLineSerializer


@login_required
def invoice_list(request):
    invoices = Invoice.objects.all().select_related('contact', 'company')
    return render(request, 'invoices/list.html', {'invoices': invoices})


@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoices/detail.html', {'invoice': invoice})
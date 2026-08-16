from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/invoices', views.InvoiceViewSet)
router.register(r'api/invoice-lines', views.InvoiceLineViewSet)

app_name = 'invoices'
urlpatterns = [
    path('', views.invoice_list, name='list'),
    path('<int:pk>/', views.invoice_detail, name='detail'),
    path('', include(router.urls)),
]
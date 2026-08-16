from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('leads/', include('leads.urls')),
    path('deals/', include('deals.urls')),
    path('tasks/', include('tasks.urls')),
    path('products/', include('products.urls')),
    path('invoices/', include('invoices.urls')),
    path('tally/', include('tally.urls')),
    path('', include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
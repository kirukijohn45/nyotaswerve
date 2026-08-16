from django.urls import path
from . import views

app_name = 'tally'
urlpatterns = [
    path('', views.tally_dashboard, name='dashboard'),
    path('test/', views.test_tally_connection, name='test_connection'),
    path('sync-ledgers/', views.sync_ledgers, name='sync_ledgers'),
]
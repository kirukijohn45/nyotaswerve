from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/leads', views.LeadViewSet)
router.register(r'api/lead-sources', views.LeadSourceViewSet)

app_name = 'leads'
urlpatterns = [
    path('', views.lead_list, name='list'),
    path('<int:pk>/', views.lead_detail, name='detail'),
    path('', include(router.urls)),
]
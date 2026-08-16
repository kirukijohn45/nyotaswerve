from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/contacts', views.ContactViewSet)
router.register(r'api/companies', views.CompanyViewSet)

app_name = 'contacts'
urlpatterns = [
    path('', views.contact_list, name='list'),
    path('<int:pk>/', views.contact_detail, name='detail'),
    path('', include(router.urls)),
]
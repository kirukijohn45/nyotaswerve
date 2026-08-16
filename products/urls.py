from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet)
router.register(r'api/categories', views.CategoryViewSet)

app_name = 'products'
urlpatterns = [
    path('', views.product_list, name='list'),
    path('', include(router.urls)),
]
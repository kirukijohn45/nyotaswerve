from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/tasks', views.TaskViewSet)

app_name = 'tasks'
urlpatterns = [
    path('', views.task_list, name='list'),
    path('<int:pk>/', views.task_detail, name='detail'),
    path('', include(router.urls)),
]
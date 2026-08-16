from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/pipelines', views.PipelineViewSet)
router.register(r'api/pipeline-stages', views.PipelineStageViewSet)
router.register(r'api/deals', views.DealViewSet)

app_name = 'deals'
urlpatterns = [
    path('', views.deal_list, name='list'),
    path('kanban/', views.kanban_board, name='kanban'),
    path('kanban/<int:pipeline_id>/', views.kanban_board, name='kanban_pipeline'),
    path('<int:pk>/', views.deal_detail, name='detail'),
    path('<int:pk>/update-stage/', views.update_deal_stage, name='update_stage'),
    path('', include(router.urls)),
]
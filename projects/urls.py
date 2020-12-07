from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = "projects"
urlpatterns = [
    path('', views.ProjectIndex.as_view()),
    path('<int:pk>/', views.ProjectDetail.as_view(), name='detail'),
    path('test', views.test_endpoint),
    path('api_call', views.ApiCalls.as_view(), name="api_results")
]
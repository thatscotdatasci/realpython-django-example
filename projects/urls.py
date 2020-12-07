from django.urls import path

from . import views


app_name = "projects"
urlpatterns = [
    path('', views.ProjectIndex.as_view()),
    path('test', views.test_endpoint)
]
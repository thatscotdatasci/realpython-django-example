from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.BlogIndex.as_view(), name="index"),
    path("<int:pk>/", views.BlogDetail.as_view(), name="detail"),
    path("<str:category>/", views.BlogCategoryIndex.as_view(), name="category")
]

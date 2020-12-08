from django.urls import path, include, reverse
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from . import views

app_name = "users"
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    # NOTE: Ensure this is in the urls.py of the configuration app
    # path('users/accounts/', include("django.contrib.auth.urls")),
]

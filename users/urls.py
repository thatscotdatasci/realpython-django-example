from django.urls import path, include, reverse
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from . import views

app_name = "users"
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('info/', views.user_info, name="info"),
    path('private_area/', views.private_area, name="private_area"),
    path('staff_area/', views.staff_area, name="staff_area"),
    path('add_messages/', views.add_messages, name="add_messages"),
    path('register/', views.register, name="register"),
    # NOTE: Ensure this is in the urls.py of the configuration app
    # https://stackoverflow.com/questions/30821412/reverse-for-password-change-done-with-arguments-and-keyword-arguments
    # path('users/accounts/', include("django.contrib.auth.urls")),
    # path('users/oauth/', include("social_django.urls"))
]

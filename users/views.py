import functools
import operator

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CustomUserCreationForm

# Create your views here.


def dashboard(request):
    return render(request, "users/dashboard.html")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")


@login_required
def private_area(request):
    return HttpResponse(
        f"Members only area; you are logged in as: {request.user.username}",content_type="text/plain"
    )


@user_passes_test(lambda user: user.is_staff)
def staff_area(request):
    return HttpResponse(
        f"Staff only area; you are logged in as: {request.user.username}", content_type="text/plain"
    )


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("users:dashboard"))
        context = {
            "error_message": functools.reduce(operator.concat, form.errors.values()),
            "form": form
        }
        return render(request, "users/register.html", context, status=400)


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello, {username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")
    return HttpResponse("Messages added", content_type="text/plain")

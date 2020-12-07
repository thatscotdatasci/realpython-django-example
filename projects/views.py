from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Project

# Create your views here.


def test_endpoint(request):
    return HttpResponse("<h1>Success</h1>")


class ProjectIndex(generic.ListView):
    model = Project
    paginate_by = 10
    template_name = "projects/index.html"
    ordering = ["title"]

import datetime

import requests
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.views import generic

from .models import Project
from .mixins import ProjectImageContextMixin

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def test_endpoint(request):
    return HttpResponse("<h1>Success</h1>")


class ProjectIndex(ProjectImageContextMixin, generic.ListView):
    model = Project
    paginate_by = 10
    template_name = "projects/index.html"
    ordering = ["title"]


class ProjectDetail(ProjectImageContextMixin, generic.DetailView):
    model = Project
    template_name = "projects/detail.html"


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ApiCalls(generic.TemplateView):
    template_name = 'projects/api_monitor.html'

    BASE_URL = 'https://httpbin.org/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{self.BASE_URL}/delay/2')
        response.raise_for_status()
        context['content'] = 'Results received!'
        context['current_time'] = datetime.datetime.now()
        return context

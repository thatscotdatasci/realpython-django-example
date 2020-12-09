from django.shortcuts import redirect
from django.http import HttpResponse


def index(request):
    return redirect("projects:index")


def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:
    
        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")

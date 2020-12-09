from django.http import HttpResponse


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

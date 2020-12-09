from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test


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

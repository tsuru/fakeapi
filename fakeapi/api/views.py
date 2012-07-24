from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def add_instance(request):
    return HttpResponse(status=201)


@require_http_methods(["DELETE"])
def remove_instance(request, name):
    return HttpResponse()


@require_http_methods(["POST"])
def bind(request, name):
    return HttpResponse(status=201)

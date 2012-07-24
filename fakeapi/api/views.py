from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["POST"])
def add_instance(request):
    return HttpResponse(status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
def remove_instance(request, name):
    return HttpResponse()


@csrf_exempt
@require_http_methods(["POST"])
def bind(request, name):
    return HttpResponse(status=201)


@csrf_exempt
@require_http_methods(["POST", "DELETE"])
def bind_or_remove_instance(request, name):
    if request.method == "POST":
        return bind(request, name)
    if request.method == "DELETE":
        return remove_instance(remove_instance, name)


@csrf_exempt
@require_http_methods(["DELETE"])
def unbind(request, name, host):
    return HttpResponse()


@require_http_methods(["GET"])
def status(request, name):
    return HttpResponse(status=204)

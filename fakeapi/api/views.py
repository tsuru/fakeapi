from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


#def create_ec2_instance(ec2_client, instance):
# #    receives an instance object
# #    the creation and population of the instance is responsibility of the api
# #    it's common to record it in the database, the the api can track more easily
# #    it's instances data
#    if not ec2_client.run(instance):
#       raise Exception("Failed to create EC2 instance.")
# #   do success stuff


@csrf_exempt
@require_http_methods(["POST"])
def add_instance(request):
    # if you need to create vms, use the commented code below
    # you must have a model Instance with a name field to use this code
    # instance = Instace()
    # instance.name = "something from request"
    # ec2_client = crane_ec2.Client()
    # try:
    #    create_ec2_instance(ec2_client, instance)
    #    instance.save()
    #   # do success stuff
    # except Exception:
    #   # do failure stuff
    #     pass
    return HttpResponse(status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
def remove_instance(request, name):
    # try:
    #     instance = Instace.objects.get(name="something from request")
    # except Instance.DoesNotExist:
    #     HttpResponse(status=404)
    # ec2_client = crane_ec2.Client()
    # try:
    #     ec2_client.terminate(instance)
    #   # ...remove from database...
    #   # do success stuff
    # except Exception:
    #   # do failure stuff
    #     pass
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

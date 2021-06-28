from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Config
from .serializers import ConfigSerializer
from django.views.decorators.csrf import csrf_exempt 
from .tasks import demo_task
import os
from configparser import ConfigParser

@csrf_exempt
def configs(request):
    
    if request.method == 'GET':
        configs = Config.objects.all()
        serializer = ConfigSerializer(configs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ConfigSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=404)

@csrf_exempt
def configByID(request, id):
    
    if request.method == 'GET':        
        try:
            configs = Config.objects.get(id=id)
            serializer = ConfigSerializer(configs, many=False)
            return JsonResponse(serializer.data, safe=False)
        except Config.DoesNotExist:
            response = {
            "config does not Exist": id
            }
            return JsonResponse(response)

    if request.method == 'DELETE':
        try:
            response = Config.objects.filter(id=id).delete()            
            return JsonResponse(response, safe=False)

        except Config.DoesNotExist:
            response = {
            "config does not Exist": id
            }
            return JsonResponse(response)

@csrf_exempt
def version(request):
    #Read config.ini file    
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

    print(config_file)
    
    config_object = ConfigParser()
    config_object.read(config_file)
    config_object.sections()

    taurus_info = config_object["TAURUS"]

    version = taurus_info["version"]


    if request.method == 'GET':
        response = {
            "name": "taurus",
            "version": version
        }
        return JsonResponse(response, status=200)

@csrf_exempt
def task(request):

    #Read config.ini file    
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

    config_object = ConfigParser()
    config_object.read(config_file)
    config_object.sections()

    ethereum_info = config_object["ETHEREUM"]

    url = ethereum_info["url"] + ":" + ethereum_info["port"]

    status = check_connection(url)
    print('working')
    print(status)
    demo_task('i am working now')
    print('returning')
    return JsonResponse({}, status=302)
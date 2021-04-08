from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Config
from .serializers import ConfigSerializer
from django.views.decorators.csrf import csrf_exempt 
from .tasks import demo_task


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
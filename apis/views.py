from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Config
from .serializers import ConfigSerializer
from django.views.decorators.csrf import csrf_exempt 
from .tasks import demo_task
from .eth_listners import check_connection, print_time, log_loop
from web3 import Web3
import json

from threading import Thread
# Create your views here.

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
            #RUN A THREAD TO LISTEN THIS CONFIG
            try:
               w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
               contractAddress = w3.toChecksumAddress(serializer.data['contractAddress'])

               abiJson = json.dumps(serializer.data['abi'])

               contract = w3.eth.contract(address=contractAddress, abi=abiJson)
               block_filter = w3.eth.filter({'fromBlock':'latest', 'address':contractAddress})
               t = Thread(target=log_loop, args=(block_filter, serializer.data['interval'], contract))
               t.start()
               print("Thread created")
            except Exception as e: 
               print(e)
               print("Error: unable to start thread")

            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=404)

def task(request):
    status = check_connection('http://localhost:8545')
    print('working')
    print(status)
    demo_task('i am working now')
    print('returning')
    return JsonResponse({}, status=302)

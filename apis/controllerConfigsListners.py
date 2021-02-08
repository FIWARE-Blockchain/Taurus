from .models import Config
from .serializers import ConfigSerializer
from .eth_listners import handle_event
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor
import json
import time

def listnerLoop():
    #TODO - CHANGE URL TO A VARIABLE IN CONFIG
    try:
        w3 = Web3(Web3.HTTPProvider('http://46.17.108.87:8545'))
        print (w3.isConnected())
    except Exception as e: 
        print("Web3 connection error!")
        print(e)

    poll_interval = 10    
    executor = ThreadPoolExecutor(max_workers=5)

    while True:
        configs = Config.objects.all()        
        serializer = ConfigSerializer(configs, many=True)
        jsonConfigs = json.dumps(serializer.data)

        json_object = json.loads(jsonConfigs)
        for element in json_object:
            try:
                print ("Id: " + str(element['id']))
                contractAddress = w3.toChecksumAddress(element['contractAddress'])
                abiStr = element['abi']
                abiStr = abiStr.replace("\'", "\"")
                abiStr = abiStr.lower()              
                abiJson = json.loads(abiStr)                  
                block_filter = w3.eth.filter({'fromBlock':'latest', 'address':contractAddress})            
                contract = w3.eth.contract(address=contractAddress, abi=abiJson)
                
                task = executor.submit(handle_event(block_filter, contract))
                
            except Exception as e: 
                print(e)
                print("Error: creating contract")

        time.sleep(poll_interval)


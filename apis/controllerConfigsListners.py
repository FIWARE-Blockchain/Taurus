from .models import Config
from .serializers import ConfigSerializer
from .eth_listners import handle_event
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor
import json
import time
import traceback 

def listnerLoop():
    #TODO - CHANGE URL TO A VARIABLE IN CONFIG
    url = "http://46.17.108.87:8545"
    try:
        w3 = Web3(Web3.HTTPProvider(url, request_kwargs={'timeout': 60}))
        print ("Connection in " + url + " :"+ str(w3.isConnected()))

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
                contractAddress = w3.toChecksumAddress(element['contractAddress'])

                print ("Id: " + str(element['id']) + "\n Address: " + str(contractAddress))

                abiStr = element['abi']
                abiStr = abiStr.replace("\'", "\"")
                abiStr = abiStr.replace("True", "true")
                abiStr = abiStr.replace("False", "false")
              
                abiJson = json.loads(abiStr)                         
                contract = w3.eth.contract(address=contractAddress, abi=abiJson)
                
                #block_filter = w3.eth.filter({'fromBlock':0})
                #block_filter = w3.eth.filter({'fromBlock':'latest', 'address':contractAddress})

                block_filter = w3.eth.filter({'fromBlock':"0x0", 'address':contractAddress})

                #block_filter = contract.events.LogEvent.createFilter(fromBlock="0x0", toBlock='latest')            
                   
                task = executor.submit(handle_event(block_filter, contract, w3))
                
            except Exception as e: 
                print("Error: creating contract")
                traceback.print_exc()

        print("----------------")
        time.sleep(poll_interval)


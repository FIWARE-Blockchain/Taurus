from .models import Config
from .serializers import ConfigSerializer
from .eth_listners import handle_event
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor
from configparser import ConfigParser
import json
import time
import traceback
import os


def listnerLoop():
    #Read config.ini file    
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

    config_object = ConfigParser()
    config_object.read(config_file)
    config_object.sections()

    ethereum_info = config_object["ETHEREUM"]

    url = ethereum_info["url"] + ":" + ethereum_info["port"]
    try:
        w3 = Web3(Web3.HTTPProvider(url, request_kwargs={'timeout': 60}))
        print ("Connection in " + url + " :"+ str(w3.isConnected()))

    except Exception as e: 
        print("Web3 connection error!")
        print(e)

    poll_interval = 10    
    executor = ThreadPoolExecutor(int(config_object["THREAD"]["max_workers"]))


    orion_info = config_object["ORION"]
    orion_endpoint= orion_info["url"] + ":" + orion_info["port"]

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
                   
                task = executor.submit(handle_event(block_filter, contract, w3, orion_endpoint))
                
            except Exception as e: 
                print("Error: creating contract")
                traceback.print_exc()

        print("----------------")
        time.sleep(poll_interval)


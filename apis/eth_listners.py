from web3 import Web3
import time
from .sender import sendToOrion
import traceback
from web3.logs import IGNORE

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
    
def handle_event(event_filter, contract, w3, orionUrl):

    print ("Length: " + str(len(event_filter.get_all_entries())))

    for event in event_filter.get_all_entries():
      try:

        receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])

        result = contract.events.LogEvent().processReceipt(receipt, errors=IGNORE)
        print(result[0]['args'])
        print(result)

        result1 = contract.events.LogOtherEvent().processReceipt(receipt, errors=IGNORE)
        print(result1)

        sendToOrion(result[0]['args'], orionUrl)

      except Exception as e: 
        print (e)
        #traceback.print_exc()
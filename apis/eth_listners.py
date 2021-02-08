from web3 import Web3
import time
from .sender import sendToOrion

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


def check_connection(url):
    w3 = Web3(Web3.HTTPProvider(url))
    # main(w3)
    return w3.isConnected()
    
def handle_event(event_filter, contract):
    for event in event_filter.get_new_entries():
      try:
        receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
        result = contract.events.greeting.processReceipt(receipt)
        print("Result: " + result[0]['args'])
        sendToOrion(result[0]['args'])

      except Exception as e: 
        print(e)
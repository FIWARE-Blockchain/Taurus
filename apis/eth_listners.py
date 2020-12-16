from web3 import Web3
import time

def check_connection(url):
    w3 = Web3(Web3.HTTPProvider(url))
    # main(w3)
    return w3.isConnected()
    

def handle_event(event):
    print(event)

def handle_event(event):
    print(event)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

def main(w3):
    block_filter = w3.eth.filter('latest')
    log_loop(block_filter, 2)
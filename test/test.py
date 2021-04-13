import json

from django.test import TestCase
from django.test.client import Client
from apis.sender import sendToOrion
from apis.eth_listners import handle_event



class TaurusTestCase(TestCase):    
    
    def setUp(self):
        pass

    def test_send_data_to_orion(self):
        data = {
                    "entities": [
                        {
                            "type": "Store",
                            "isPattern": "false",
                            "id": "urn:ngsi-ld:Store:001"
                        }
                    ],
                    "attrs": [
                        "temperature"
                    ]
                } 
        url = "http://localhost:1026"
        try:
            response = sendToOrion(data, url)      
            self.assertEqual(response.status_code, 200)
        except Exception as e: 
            print (e)

    def test_get_config(self):
        response = self.client.get("http://localhost:8000/config/")
        self.assertEqual(response.status_code, 200)

    def test_post_config(self):
        body = {
               "id":"event-identifier",
               "interval": 10,
               "contractAddress":"0x1349f3e1b8d71effb47b840594ff27da7e603d17",
               "abi": [
            {
            "inputs": [
            {
            "name": "_x",
            "type": "uint256"
            }
            ],
            "anonymous": False,
            "name": "LogEvent",
            "type": "event"
            },
            {
            "inputs": [
            {
            "indexed": True,
            "name": "_sender",
            "type": "address"
            }
            ],
            "anonymous":False,
            "name": "LogOtherEvent",
            "type": "event"
            }
            ]
            }
        response = self.client.post("http://localhost:8000/config/",
                                json.dumps(body),
                                content_type="application/json")
        self.assertEqual(response.status_code, 201)



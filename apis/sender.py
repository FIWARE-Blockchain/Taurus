import json
import requests

def sendToOrion(data): 
	orion_endpoint="http://localhost:1026/"

	url_query=(orion_endpoint + "/v1/contextEntities")
	# body_dict = {
		  
	#      "type":"Transaction",
	#      "isPattern":"false",
	#      "id":"tr0002",
	#      "attributes":[  
	#         {  
	#            "name":"transactionType",
	#            "type":"String",
	#            "value":"TransferLand"
	#         },
	#         {  
	#            "name":"VendorPublicKey",
	#            "type":"float",
	#            "value":"-5.809901"
	#         },
	#         {  
	#            "name":"BuyerPublicKey",
	#            "type":"float",
	#            "value":"-8.809901"
	#         },
	#         {  
	#            "name":"LandPublicKey",
	#            "type":"float",
	#            "value":"-5.809901"
	#         },
	#         {  
	#            "name":"Value",
	#            "type":"float",
	#            "value":"350000"
	#         }
	#      ]
	  
	# }

	r_headers = {'Content-Type': 'application/json'}

	r = requests.post(
	    url=url_query,
	    data=json.dumps(data),
	    headers=r_headers
	)

	print(r.content)
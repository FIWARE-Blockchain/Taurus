import json
import os
import requests
from configparser import ConfigParser


def sendToOrion(data, url): 
	

	url_query=(url + "/v1/contextEntities")

	#TODO 
	#CHECK DATA FORMAT

	r_headers = {'Content-Type': 'application/json'}

	r = requests.post(
	    url=url_query,
	    data=json.dumps(data),
	    headers=r_headers
	)

	print(r.content)
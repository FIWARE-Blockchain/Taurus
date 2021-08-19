# API DESCRIPTION 
## META

### Get the status

```sh
curl --location --request GET 'http://localhost:8000/version'
```
**Response**

```json
{
    "name": "taurus",
    "version": "0.0.1"
}
```
 
## CONFIG
 
### Get All the configs

```sh
curl --location --request GET 'http://localhost:8000/config'
```
 
### Get the config by ID

```sh
curl --location --request GET 'http://localhost:8000/config/16'
```
 
### Delete a config by ID

```sh
curl --location --request DELETE 'http://localhost:8000/config/17'
```
 
### Create a config

```sh 
curl --location --request POST 'http://localhost:8000/config' \
--header 'Content-Type: application/json' \
--data-raw ‘   "id":"event-identifier",
   "interval":10,
   "contractAddress":"0x1349f3e1b8d71effb47b840594ff27da7e603d17",
   "abi":[
      {
	 "inputs":[
	    {
	       "name":"_x",
	       "type":"uint256"
	    }
	 ],
	 "anonymous":false,
	 "name":"LogEvent",
	 "type":"event"
      },
      {
	 "inputs":[
	    {
	       "indexed":true,
	       "name":"_sender",
	       "type":"address"
	    }
	 ],
	 "anonymous":false,
	 "name":"LogOtherEvent",
	 "type":"event"
      }
   ]
}’  "id":"event-identifier",
   "interval":10,
   "contractAddress":"0x1349f3e1b8d71effb47b840594ff27da7e603d17",
   "abi":[
      {
	 "inputs":[
	    {
	       "name":"_x",
	       "type":"uint256"
	    }
	 ],
	 "anonymous":false,
	 "name":"LogEvent",
	 "type":"event"
      },
      {
	 "inputs":[
	    {
	       "indexed":true,
	       "name":"_sender",
	       "type":"address"
	    }
	 ],
	 "anonymous":false,
	 "name":"LogOtherEvent",
	 "type":"event"
      }
   ]
}
```

 **Response**
 
```json
{
    "id": 8,
    "contractAddress": "0x1349f3e1b8d71effb47b840594ff27da7e603d17",
    "abi": [
        {
            "inputs": [
                {
                    "name": "_x",
                    "type": "uint256"
                }
            ],
            "anonymous": false,
            "name": "LogEvent",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "indexed": true,
                    "name": "_sender",
                    "type": "address"
                }
            ],
            "anonymous": false,
            "name": "LogOtherEvent",
            "type": "event"
        }
    ],
    "interval": 10
}
```

Try out the postman collection [here](https://github.com/FIWARE-Blockchain/Taurus/blob/master/Taurus%20API.postman_collection.json)

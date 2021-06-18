# Taurus

Taurus is a blockchain listener that supports various DLT, and the listener aims to listen to Blockchain Events and store data in FIWARE. This component compliments FIWARE as an OffChainDB.

## Architecture


TAURUS IN POWERED BY FIWARE ARCHITECTURE


### Flow Diagram
 
The way Taurus work's in 'Powered By FIWARE' architecture as follows:



1. A post request "/config" from the user consists of the contract Address and attributes to listen to when a new transaction was added in a DLT.
2. Taurus creates a new listener in the background to listen to the DLT according configuration requested.
3. When a new transaction is added with the same contract Address previously  registered, a listener captures this information and sends it to FIWARE context Broker.


SUPPORTED DLT CLIENTS
[x] Ethereum
[  ] IOTA
[  ] FABRIC Chaincode
 
DEPENDENCIES:

This project uses: python3 and pip3

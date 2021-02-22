# Taurus - FIWARE Blockchain Listner

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4661/badge)](https://bestpractices.coreinfrastructure.org/projects/4661)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Taurus is a blockchain listner that supports various DLT, the listner aims to listen Blockchain Events and store data in FIWARE. This component compliments FIWARE as an OffChainDB.


|  <img src="https://assets.getpostman.com/common-share/postman-logo-stacked.svg" align="center" height="25"> [Postman Collections](https://documenter.getpostman.com/view/487008/TWDXpciC) | 

|---- | --- |
# Architecture
## Taurus Architecture
![Taurus Architecture](https://github.com/FIWARE-Blockchain/Taurus/tree/master/docs/images/architecture.png)

## Supported DLT Clients
- [x] Ethereum 
- [ ] IOTA
- [ ] FABRIC Chaincode

### Dependencies
_This project uses:_
 - python3
 - pip3

### Installation guide - Localhost

1. Install python3 and pip3
2. Run following commands:
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver --noreload

### Installation guide - Docker

1. Install Docker
2. Run following commands:
docker build -t taurus .
docker run taurus

### Configuration
Send a POST request to add a new listener configuration according to the Postman Collection example.


## License

CanisMajor is licensed under the [MIT](LICENSE) License.

© 2021 FIWARE Foundation e.V.

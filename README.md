# Taurus - FIWARE DLT Listner

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![CodeQL](https://github.com/FIWARE-Blockchain/Taurus/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/FIWARE-Blockchain/Taurus/actions/workflows/codeql-analysis.yml)
[![publish mkdocs](https://github.com/FIWARE-Blockchain/Taurus/actions/workflows/documentation.yml/badge.svg)](https://github.com/FIWARE-Blockchain/Taurus/actions/workflows/documentation.yml)

Taurus is a DLT listener that supports various blockchain and DLT, and the listener aims to listen to events and store data in FIWARE. This component compliments FIWARE as an OffChainDB.


|  <img src="https://assets.getpostman.com/common-share/postman-logo-stacked.svg" align="center" height="25"> [Postman Collections](https://documenter.getpostman.com/view/487008/TWDXpciC) | 

# Architecture
## Taurus Architecture
<img src="https://github.com/FIWARE-Blockchain/Taurus/blob/master/docs/images/architecture.png" width="700">

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
```
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver --noreload
```

### Installation guide - Docker

1. Install Docker
2. Run following commands:
```
docker build -t taurus .
docker run taurus
```

### Running tests
1. Install python3 and pip3
2. Run following commands:
```
pip3 install -r requirements.txt
python3 manage.py test
```


### Configuration
Send a POST request to add a new listener configuration according to the Postman Collection example.


## License

CanisMajor is licensed under the [MIT](LICENSE) License.

© 2021 FIWARE Foundation e.V.

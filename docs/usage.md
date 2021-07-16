# Usages

##CREATION OF A NEW LISTENER
ADD sequence diagram



##INSTALLATION GUIDE
This section describes installing Taurus Blockchain Listener in two different ways:
 
###1 -LOCALHOST
REQUIREMENTS
In order to execute Taurus, it is needed to have previously installed the following software:
Install python3 and pip3
 
CLONE PROJECT
git clone https://github.com/FIWARE-Blockchain/Taurus
  
CONFIGURE DLT AND ORION URL (IT'S SHOULD ALREADY RUNNING)
at apis/config.ini
 
[ETHEREUM]
url = http://46.17.108.87
port = 8545
 
[ORION]
url = http://localhost
port = 1026
 
[THREAD]
max_workers = 5
 
INSTALL DEPENDENCIES
pip3 install -r requirements.txt
 
RUN
python3 manage.py migrate
python3 manage.py runserver --noreload
 
RUN TEST
Install python3 and pip3
pip3 install -r requirements.txt
python3 manage.py test
 
###2 -DOCKER
REQUIREMENTS
In order to execute Taurus, it is needed to have previously installed the following software:
Install Docker
  
CLONE PROJECT
git clone https://github.com/FIWARE-Blockchain/Taurus
 
CONFIGURE DLT AND ORION URL (IT'S SHOULD ALREADY RUNNING)
at apis/config.ini
 
[TAURUS]
version = 0.0.1
port = 8080
 
[ETHEREUM]
url = http://46.17.108.87
port = 8545
 
[ORION]
url = http://localhost
port = 1026
 
[THREAD]
max_workers = 5
 
RUN
docker build -t taurus .
docker run taurus

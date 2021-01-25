const Web3 = require('web3');
const contract = require('truffle-contract');
const agrifood_artifact = require('../build/contracts/Agrifood.json');
var AgrifoodWeb3 = contract(agrifood_artifact);
var solc = require('solc');
const path = require('path');
const fs = require('fs');
const config = require('../config');
const axios = require('axios');
var web3 = new Web3();

/*
connect web3 provider
*/
web3.setProvider(new web3.providers.HttpProvider(`${config.RPC_URL}`));

/*
read and compile the contract
*/
const contracts = path.resolve(__dirname, '..', 'contracts', 'Agrifood.sol');
const source = fs.readFileSync(contracts, 'UTF-8');
const output = solc.compile(source.toString(), 1);
web3.eth.defaultAccount = web3.eth.accounts[0];
let AgrifoodContract = web3.eth.contract(agrifood_artifact.abi);

// Smart contract EVM bytecode as hex
let code = '0x' + agrifood_artifact.bin;

/*
deploy contract
*/
const deployContract = AgrifoodContract.new({ from: web3.eth.coinbase, gas: 1000000, data: code }, function (err, res) {
  if (!err) {
    transactionHash = deployContract.transactionHash;
    let recipt = web3.eth.getTransactionReceipt(deployContract.transactionHash);
    if (recipt && recipt.contractAddress) {
      // set contract address env  
      process.env.CONTRACT_ADDRESS = recipt.contractAddress;
      console.log("recipt" + JSON.stringify(recipt));
    }
  }
});

module.exports = {
  start: function (success, error) {
    var self = this;
    AgrifoodWeb3.setProvider(self.web3.currentProvider);
    self.web3.eth.getAccounts(function (err, accs) {
      if (err != null) {
        error("There was an error fetching your accounts.");
        return;
      }
      if (accs.length == 0) {
        error("Couldn't get any accounts! Make sure your Ethereum client is configured correctly.");
        return;
      }
      self.accounts = accs;
      success(self.accounts);
    });
  },

  createAsset: function (body, _success, _error) {
    try {
      web3.eth.defaultAccount = body.address;
      var contract = web3.eth.contract(agrifood_artifact.abi);
      var myContract = contract.at(process.env.CONTRACT_ADDRESS);
      console.log('process.env.CONTRACT_ADDRESS', process.env.CONTRACT_ADDRESS);
      var response = myContract.addAsset(body.id, body.name, body.type, body.description, body.owner, (body.hasParent) ? body.hasParent : '');
      _success({ transactionHash: response, Address: web3.eth.defaultAccount })
    }
    catch (err) {
      _error(err);
    }
  },

  SubmitAndUpdateContext: function (body) {
    let address = '';
    if (body.owner.value === 'ff_farm') {
      address = web3.eth.accounts[0];
    }
    if (body.owner.value === 'bio_pasta') {
      address = web3.eth.accounts[1];
    }
    try {
      web3.eth.defaultAccount = address;
      var contract = web3.eth.contract(agrifood_artifact.abi);
      var myContract = contract.at(process.env.CONTRACT_ADDRESS);
      var response = myContract.addAsset(body.id, body.name.value, body.type, body.description.value, body.owner.value, (body.hasAgriProductTypeParent.value) ? body.hasAgriProductTypeParent.value : '');
      if(response) {
        // update context broker
        axios.patch(config.CONTEXT_BROKER + '/v2/entities/' + body.id + '/attrs',
        {
            "address": {
                "value": web3.eth.defaultAccount.toString(),
                "type": "String"
            },
            "transactionHash": {
                "value": response.toString(),
                "type": "String"
            }
        }).then((res) => {
          console.log('broker updated' + JSON.stringify(res));
        }).catch((err) => {
          console.log('error ' + JSON.stringify(err));
        })
      }
    }
    catch (err) {
      console.log('err' + JSON.stringify(err));
    }
  }
}

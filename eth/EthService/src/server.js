const express = require('express');
const app = express();
const Web3 = require('web3');
const bodyParser = require('body-parser');
const config = require('../config');
const routes = require('./api');
const truffle_connect = require('./app');
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());
// api routes
app.use('/',routes);
//expose applicaion
app.listen(config.PORT, () => {
  // fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
  truffle_connect.web3 = new Web3(new Web3.providers.HttpProvider(`${config.RPC_URL}`));
  console.log("Express Listening at http://localhost:" + config.PORT);
});

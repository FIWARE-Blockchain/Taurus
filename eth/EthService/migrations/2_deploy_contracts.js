var Agrifood = artifacts.require("./Agrifood.sol");

module.exports = function(deployer) {
  deployer.deploy(Agrifood);
};
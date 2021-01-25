// Allows us to use ES6 in our migrations and tests.
require('babel-register')

module.exports = {
  networks: {
    development: {
      host: 'localhost',
      port: 8545,
      network_id: '*'
    }
  },
  compilers: {
    solc: {
      version: '0.4.25'
    }
 }
}

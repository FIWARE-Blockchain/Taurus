const PORT = process.env.PORT || 3002;
const RPC_URL = process.env.RPC_URL || 'http://localhost:8545';
const CONTEXT_BROKER = process.env.CONTEXT_BROKER || "http://localhost:1026";

module.exports = {
    PORT,
    RPC_URL,
    CONTEXT_BROKER
}
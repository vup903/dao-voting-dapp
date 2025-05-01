# DAO Voting DApp (Python + Flask + Solidity)

This is a fully functional decentralized voting application built with:

- Solidity smart contracts on the Ethereum blockchain  
- Python Flask backend using `web3.py` to interact with the contract  
- Ethereum wallet support via Metamask  
- JSON APIs to create proposals, vote, and query results

## Features

- Anyone can view proposals and vote with their Ethereum wallet  
- Only the contract owner can create new proposals and execute results  
- All votes and proposals are publicly accessible  
- Lightweight and easy to run locally

## Tech Stack

- Smart Contract: Solidity  
- Blockchain: Ethereum (Goerli testnet)  
- Backend: Python + Flask  
- Web3 Integration: web3.py  
- Deployment: Flask server and `.env` for secrets

## How to Run

1. Install Python dependencies:

```bash
cd backend
pip install flask web3 python-dotenv
```

2. Deploy the smart contract (via Remix or Hardhat).  
   Copy the deployed contract address and ABI, then update `.env` as shown in `.env.example`:

```
WEB3_PROVIDER=https://eth-goerli.g.alchemy.com/v2/your_key
CONTRACT_ADDRESS=0xYourContractAddress
OWNER_ADDRESS=0xYourWallet
PRIVATE_KEY=your_private_key
```

3. Start the Flask server:

```bash
python app.py
```

## API Endpoints

- `GET /proposals`: Retrieve all proposals  
- `POST /create`: Create a new proposal (only the contract owner can do this)  
- `POST /vote`: Vote on a proposal (requires voter's wallet address and private key)

## Sample Request for Voting

```json
{
  "proposalId": 0,
  "support": true,
  "voter": "0xYourVoterAddress",
  "privateKey": "your_voter_private_key"
}
```

## License

MIT © 2025

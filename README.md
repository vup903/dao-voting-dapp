# DAO Voting DApp (Python + Flask Edition) 🗳️

A simple decentralized voting system using Solidity + Flask backend + web3.py

## 🧠 Stack

- Solidity for smart contracts
- Flask (Python) backend with web3.py
- Ethereum (Goerli testnet)

## 🔧 Setup

### 1. Install Python dependencies

```bash
cd backend
pip install flask web3 python-dotenv
```

### 2. Compile and Deploy Smart Contract

Use Hardhat or Remix to deploy `DaoVoting.sol`. Then, set `.env` with your contract info:

```
WEB3_PROVIDER=https://eth-goerli.g.alchemy.com/v2/your_alchemy_key
CONTRACT_ADDRESS=0xYourContractAddress
OWNER_ADDRESS=0xYourWalletAddress
PRIVATE_KEY=your_private_key
```

### 3. Start Flask server

```bash
python app.py
```

### 4. API Endpoints

- `GET /proposals` - List all proposals
- `POST /create` - Create a proposal (owner only)
- `POST /vote` - Vote on a proposal (send voter address + private key)

## ✨ Sample vote request body

```json
{
  "proposalId": 0,
  "support": true,
  "voter": "0xYourVoterAddress",
  "privateKey": "voter_private_key"
}
```

## 📄 License

MIT

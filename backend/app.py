from flask import Flask, request, jsonify
from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER")))
with open("backend/DaoVotingABI.json") as f:
    abi = json.load(f)

contract_address = Web3.to_checksum_address(os.getenv("CONTRACT_ADDRESS"))
contract = w3.eth.contract(address=contract_address, abi=abi)
account = Web3.to_checksum_address(os.getenv("OWNER_ADDRESS"))
private_key = os.getenv("PRIVATE_KEY")

@app.route("/proposals", methods=["GET"])
def get_proposals():
    count = contract.functions.proposalCount().call()
    result = []
    for i in range(count):
        p = contract.functions.getProposal(i).call()
        result.append({
            "id": p[0],
            "description": p[1],
            "yesVotes": p[2],
            "noVotes": p[3],
            "executed": p[4],
        })
    return jsonify(result)

@app.route("/create", methods=["POST"])
def create_proposal():
    desc = request.json["description"]
    nonce = w3.eth.get_transaction_count(account)
    tx = contract.functions.createProposal(desc).build_transaction({
        'from': account,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })
    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return jsonify({"tx_hash": tx_hash.hex()})

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    pid = data["proposalId"]
    support = data["support"]
    voter = Web3.to_checksum_address(data["voter"])
    voter_key = data["privateKey"]

    nonce = w3.eth.get_transaction_count(voter)
    tx = contract.functions.vote(pid, support).build_transaction({
        'from': voter,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })
    signed = w3.eth.account.sign_transaction(tx, voter_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return jsonify({"tx_hash": tx_hash.hex()})

if __name__ == "__main__":
    app.run(debug=True)

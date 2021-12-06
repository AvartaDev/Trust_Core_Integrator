from flask import Flask, request
import json
from waitress import serve
import walletcore as core


wrapper_server = Flask(__name__)

@wrapper_server.route('/bitcoin/create-wallet', methods=['POST'])
def bitcoin_create_wallet():
    wallet = core.HDWallet.create(128, 'abcdefghijklmnopqrstuvwxyz')
    mnemonic = wallet.mnemonic
    entropy = wallet.entropy
    address = wallet.get_address_for_coin(core.CoinType.Bitcoin)

    return json.dumps({"status": True, "BTC wallet address": address, "mnemonic": mnemonic})

@wrapper_server.route('/bitcoin/sign-transaction', methods=['POST'])
def bitcoin_sign_transaction():
    postData = request.json
    msg = postData.get('message')

    return json.dumps({"status": True, "BTC wallet address": address, "mnemonic": mnemonic})

# wrapper_server.run(port = 3000)
serve(wrapper_server, host="0.0.0.0", port=8080)

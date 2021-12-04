from flask import Flask, request
import json

wrapper_server = Flask(__name__)

@wrapper_server.route('/transfer', methods=['POST'])
def transfer():
    postData = request.json
    print(postData)
    msg = postData.get('message')

    socketio.emit('message', {'msg': msg})

    return json.dumps({"status": True})
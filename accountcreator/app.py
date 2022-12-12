from flask import request, Flask
import json, socket

accounts = {}

import sys
sys.path.insert(0,"..")

app = Flask(__name__)

@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

# curl -d '{ "email": "user_email", "password" : "password_to_add" }' -X POST http://localhost:9003/addAccount  -H "Content-type: application/json"

@app.route('/addAccount', methods=["POST"])
def addAccount():
    user_email = request.json['email']
    password = request.json['password']
    
    if user_email not in accounts:
        accounts[user_email] = [password]
    return json.dumps(accounts)
    
# curl -d '{ "email": "user_email", "new_password" : "password_to_change" }' -X POST http://localhost:9003/changePassword  -H "Content-type: application/json"

@app.route('/changePassword', methods=["POST"])
def changePassowrd():
    user_email = request.json['email']
    new_password = request.json['new_password']
    
    if user_email in accounts:
        accounts[user_email] = [new_password]
    return json.dumps(accounts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)

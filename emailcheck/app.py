from flask import request, Flask
import json, socket

import sys
sys.path.insert(0,"..")

app = Flask(__name__)

#
# curl http://localhost:9000
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9000/check   -H "Content-type: application/json"
#
@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    email = request.json['email']
    number_of_at_signs = email.count("@")
    correct_address = email.count("gmail")

    returnDictionary = {}
    returnDictionary["email"] = email
    returnDictionary["at_signs"] = number_of_at_signs
    returnDictionary["address"] = correct_address

    if number_of_at_signs and correct_address == 1:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)

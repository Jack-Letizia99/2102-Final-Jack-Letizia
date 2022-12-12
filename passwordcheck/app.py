#
#
#
from flask import request, Flask
import json, socket


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
# curl -d "{ \"password\" : \"xxxxxxxx\" }" -X POST http://localhost:9001/check  -H "Content-type: application/json"
#
@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    password = request.json['password']
    password_length = len(password)
    nums = {'1','2','3','4','5','6','7','8','9','0'}
    has_number = False
    
	
    returnDictionary = {}
    returnDictionary["password"] = password
    returnDictionary["length"] = password_length
    for i in range(password_length):
    	if password[i] in nums:
            has_number = True

    	
    	    

    if password_length >= 8 and has_number == True:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)

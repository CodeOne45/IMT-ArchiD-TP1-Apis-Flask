from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3400
HOST = 'localhost'

with open('users.json'.format("."), "r") as jsf:
   db_JSON = json.load(jsf)


users = db_JSON["users"]

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the User service!</h1>",  200)

# to test templates of Flask
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for User service'),200)

# get the complete json file
@app.route("/jsonusers", methods=['GET'])
def get_json():
    #res = make_response(jsonify(INFO), 200)

    res =  make_response(jsonify(db_JSON), 200)
    res = res
    return res

# get the user by its id
@app.route("/users/booking", methods=['GET'])
def get_user_by_id():
    json = ""
    
    if request.args:
        req = request.args
        
        parameters = {
            "userid": str(req["userid"])
        }
        response = requests.get("http://localhost:3300/bookings", params=parameters)
        res = make_response(jsonify(response.json()))
        return res
    
    res = make_response(jsonify({"error":"user id not difiend"}),400)
    return response.json()
  

if __name__ == "__main__":
    print("Server running in port %s // "%(PORT))
    app.run(host=HOST, port=PORT)
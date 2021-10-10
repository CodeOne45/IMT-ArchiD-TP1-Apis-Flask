from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = '192.168.0.15'

with open('bookings.json'.format("."), "r") as jsf:
   db_JSON = json.load(jsf)

bookings = db_JSON["bookings"]
#links = db_JSON["links"]


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Booking service!</h1>",  200)

# to test templates of Flask
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for Booking service'),200)

# get the complete json database or booking by id
@app.route("/bookings", methods=['GET'])
def get_json():
    if request.args:
        listBookingsByUser = []
        req = request.args
        for booking in bookings:        
            if str(booking["userid"]) == str(req["userid"]):
                    listBookingsByUser.append(booking)
        if not listBookingsByUser:
            res = make_response(jsonify({"error":"booking user not found"}),400)
            return res    
        res = make_response(jsonify(listBookingsByUser),200)
        return res
        
    return make_response(jsonify(db_JSON), 200)


# add a new booking to a given userID
@app.route("/bookings/<userid>", methods=["POST"]) 
def create_movie(userid):
    req = request.get_json()
    print(req)
    for booking in bookings:
        if str(booking["userid"]) == str(userid):
            #return make_response(jsonify({"error":"movie ID already exists"}),409)
            booking["dates"].append(req)
            return make_response(jsonify(booking),409)

    res = make_response(jsonify({"Error":" User ID not found"}),200)
    return res


if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    #app.run(host=HOST, port=PORT)
    app.run()
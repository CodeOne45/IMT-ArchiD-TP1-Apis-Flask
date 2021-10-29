from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3300
HOST = 'localhost'

with open('bookings.json'.format("."), "r") as jsf:
    db_JSON = json.load(jsf)

bookings = db_JSON["bookings"]
# links = db_JSON["links"]


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Booking service!</h1>",  200)

# to test templates of Flask


@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for Booking service'), 200)

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
            res = make_response(
                jsonify({"error": "booking user not found"}), 400)
            return res
        res = make_response(jsonify(listBookingsByUser), 200)
        return res

    return make_response(jsonify(db_JSON), 200)


# add a new booking to a given userID
# Todo: Verify if given movie is avalable on the given date

@app.route("/bookings/<userid>", methods=["POST"])
def create_movie(userid):
    req = request.get_json()
    print(req)
    for booking in bookings:
        if str(booking["userid"]) == str(userid):
            # return make_response(jsonify({"error":"movie ID already exists"}),409)
            booking["dates"].append(req)
            return make_response(jsonify(booking), 409)

    res = make_response(jsonify({"Error": " User ID not found"}), 200)
    return res


# delete a mobookingvie
@app.route("/bookings/<userid>", methods=["DELETE"])
def del_movie(movieid):
    movieDelete = []
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            movie.pop("links")
            movieDelete.append(movie)
            movieDelete.append(links)
            return make_response(jsonify(movieDelete), 200)

    res = make_response(jsonify({"error": "movie ID not found"}), 400)
    return res

# Get movie id with a given date date / avalables movies on a given date
# Ex : bookings/schedule/20151130
# TODO : Add this function to API doc


@app.route("/bookings/schedule/<date>", methods=['GET'])
def get_movie_by_date(date):

    req = request.args

    parameters = {
        "date": str(date)
    }
    response = requests.get(
        "http://localhost:3500/showmovies", params=parameters)
    # print(response.json()[0]["movies"][0])
    res = make_response(jsonify(response.json()))
    return res


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
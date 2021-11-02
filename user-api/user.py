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


# home page of user service


@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the User service!</h1>",  200)

# to test templates of Flask


@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for User service'), 200)


# get the complete json file


@app.route("/users", methods=['GET'])
def get_json():
    res = make_response(jsonify(db_JSON), 200)
    return res

# add a new user


@app.route("/users/add", methods=["POST"])
def create_user():
    req = request.get_json()
    for user in users:
        if str(user["id"]) == str(req["id"]):
            return make_response(jsonify({"error": "user ID already exists"}), 409)

    users.append(req)
    res = make_response(jsonify({"message": "user added"}), 200)
    return res


# delete a user
@app.route("/users/<userid>", methods=["DELETE"])
def del_user(userid):
    userDelete = []
    for user in users:
        if str(user["id"]) == str(userid):
            userDelete.append(user)
            users.remove(user)
            return make_response(jsonify(userDelete), 200)

    res = make_response(jsonify({"error": "user ID not found"}), 400)
    return res

# add a booking for a user


@app.route("/users/booking/<userid>", methods=['POST'])
def add_user_booking_by_id(userid):

    req = request.args
    response = requests.post(
        "http://localhost:3300/bookings/" + str(userid), json=request.get_json())
    res = make_response(jsonify(response.json()))
    return res


# delete a booking of a user
@app.route("/users/booking/<userid>", methods=['DELETE'])
def delete_user_booking_by_id(userid):

    req = request.args
    response = requests.delete(
        "http://localhost:3300/bookings/" + str(userid))
    res = make_response(jsonify(response.json()))
    return res


# get user by id

@app.route("/user/<userid>", methods=['GET'])
def get_user_by_id(userid):
    for user in users:
        if str(user["id"]) == str(userid):
            res = make_response(jsonify(user), 200)
            return res

    res = make_response(jsonify({"error": "user ID not found"}), 201)
    return res

# get list/json of all movies /users/movies


@app.route("/users/movies", methods=['GET'])
def get_movies_list():

    response = requests.get(
        "http://localhost:3200/json")
    res = make_response(jsonify(response.json()["movies"]))
    return res


# get a user booking(s) by his id


@app.route("/users/booking", methods=['GET'])
def get_user_booking_by_id():

    if request.args:
        req = request.args

        parameters = {
            "userid": str(req["userid"])
        }
        response = requests.get(
            "http://localhost:3300/bookings", params=parameters)
        res = make_response(jsonify(response.json()))
        return res

    res = make_response(jsonify({"error": "user id not difiend"}), 400)
    return response.json()

# get a movie infos by title/name - /users/moviebyname/{movieTitle}


@app.route("/users/moviebyname/<title>", methods=['GET'])
def get_movie_by_date(title):

    req = request.args

    parameters = {
        "title": str(title)
    }
    response = requests.get(
        "http://localhost:3200//moviesbytitle", params=parameters)
    res = make_response(jsonify(response.json()))
    return res


# TODO: get a list of avalable movie(s) id with a given date/time
@app.route("/users/movies/date/<date>", methods=['GET'])
def get_moviesid_by_date(date):

    req = request.args
    response = requests.get(
        "http://localhost:3300/bookings/schedule/" + str(date))
    print(response.text)
    res = make_response(jsonify(response.json()))
    return res


if __name__ == "__main__":
    print("Server running in port %s // " % (PORT))
    app.run(host=HOST, port=PORT)

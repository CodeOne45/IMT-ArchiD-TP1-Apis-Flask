# ------ Imports -------

from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
from werkzeug.exceptions import NotFound

# ------ Constants -------

app = Flask(__name__)

PORT = 3400
HOST = 'localhost'

BOOKING_API_URL = "http://localhost:3300/bookings/"
MOVIES_API_URL = "http://localhost:3200/"

txt_template = 'This is my HTML template for User service'
msg_root = "<h1 style='color:blue'>Welcome to the User service!</h1>"
msg_user_added = "user added"
msg_user_id_exist = "user ID already exists"
msg_user_id_not_found = "User ID not found"

#  ------ Uploads ------

with open('users.json'.format("."), "r") as jsf:
    db_JSON = json.load(jsf)

# DB
users = db_JSON["users"]

# ----- Functions for API requests ------
# TODO : Add request URL in function comments/doc


@app.route("/", methods=['GET'])
def home():
    """ This function return a html for the root page

        Returns:
            HTML: Root message
    """
    return make_response(msg_root,  200)


@app.route("/template", methods=['GET'])
def template():
    """ This function return a html page for the template root

        Returns:
            HTML: Template page message
    """
    return make_response(render_template('index.html', body_text=txt_template), 200)


@app.route("/users", methods=['GET'])
def get_json():
    """Get the complete USER JSON file

    Returns:
        JSON: Users in JSON format
    """
    res = make_response(jsonify(db_JSON), 200)
    return res


@app.route("/users/add", methods=["POST"])
def create_user():
    """ Add a new user with a given ID
    Parameters:
        id (string): New user id

    Returns:
        - JSON: Added booking in JSON format
        - message: Error message if user ID already exists 
    """
    req = request.get_json()
    for user in users:
        if str(user["id"]) == str(req["id"]):
            return make_response(jsonify({"error": msg_user_id_exist}), 409)

    users.append(req)
    res = make_response(jsonify({"message": msg_user_added}), 200)
    return res


@app.route("/users/<userid>", methods=["DELETE"])
def del_user(userid):
    """ Delete a user from a given user id

    Args:
        userid (string): User ID to delete user from DB

    Returns:
        - JSON: Deleted user details in JSON format
        - message: Error message if user ID is not found
    """
    user_delete = []
    for user in users:
        if str(user["id"]) == str(userid):
            user_delete.append(user)
            users.remove(user)
            return make_response(jsonify(user_delete), 200)

    res = make_response(jsonify({"error": msg_user_id_not_found}), 400)
    return res


@app.route("/user/<userid>", methods=['GET'])
def get_user_by_id(userid):
    """ Get user details by id

    Args:
        userid (string): Serched user id

    Returns:
         - JSON: User details in JSON format
        - message: Error message if user ID is not found
    """
    for user in users:
        if str(user["id"]) == str(userid):
            res = make_response(jsonify(user), 200)
            return res

    res = make_response(jsonify({"error": msg_user_id_not_found}), 201)
    return res


@app.route("/users/booking/<userid>", methods=['POST'])
def add_user_booking_by_id(userid):
    """ Add a new booking to a given user ID

    Args:
        userid (string): The user ID for which you must add a new booking

    Returns:
        - JSON: Added booking in JSON format
        - message: Error message if user ID not found 
    """
    response = requests.post(
        BOOKING_API_URL + str(userid), json=request.get_json())
    res = make_response(jsonify(response.json()))
    return res


@app.route("/users/booking/<userid>", methods=['DELETE'])
def delete_user_booking_by_id(userid):
    """ Dellete a booking from a given user id

    Args:
        userid (string): User ID to delete booking

    Returns:
        - JSON: Deleted booking details in JSON format
        - message: Error message if user ID is not found
    """
    response = requests.delete(
        BOOKING_API_URL + str(userid))
    res = make_response(jsonify(response.json()))
    return res


@app.route("/users/booking", methods=['GET'])
def get_user_booking_by_id():
    """ Get user booking by given ID

    Returns:
        - JSON: The booking details which correspond to the 
                user ID in JSON format
        - message: Error message if user ID doesn't exists
    """
    if request.args:
        req = request.args

        parameters = {
            "userid": str(req["userid"])
        }
        response = requests.get(
            BOOKING_API_URL, params=parameters)
        res = make_response(jsonify(response.json()))
        return res

    res = make_response(jsonify({"error": msg_user_id_not_found}), 400)
    return res.json()


@app.route("/users/movies", methods=['GET'])
def get_movies_list():
    """ Get list/json of all movies 

    Returns:
        JSON: Movies in JSON format
    """
    response = requests.get(
        MOVIES_API_URL + "json")
    res = make_response(jsonify(response.json()["movies"]))
    return res


@app.route("/users/moviebyname/<title>", methods=['GET'])
def get_movie_by_date(title):
    """ Get a movie infos by its title

    Args:
        title (string): Searched movie title

    Returns:
        - JSON: Movie details in JSON format
        - message: Error message if movie title not found
    """
    parameters = {
        "title": str(title)
    }
    response = requests.get(
        MOVIES_API_URL + "moviesbytitle", params=parameters)
    res = make_response(jsonify(response.json()))
    return res


@app.route("/users/movies/date/<date>", methods=['GET'])
def get_moviesid_by_date(date):
    """ Get movie(s) id(s) with a given date / avalables movies on a given date

    Args:
        date (string): the date to search for a movie

    Returns:
        JSON: Movie id's JSON format list
    """
    response = requests.get(
        BOOKING_API_URL + "schedule/" + str(date))
    print(response.text)
    res = make_response(jsonify(response.json()))
    return res

# Main function to launch User API/App


if __name__ == "__main__":
    print("Server running in port %s // " % (PORT))
    app.run(host=HOST, port=PORT)

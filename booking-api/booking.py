# ------ Imports -------

from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
from werkzeug.exceptions import NotFound

# ------ Constants -------

app = Flask(__name__)

PORT = 3300
HOST = 'localhost'

TIME_API_URL = "http://localhost:3500/showmovies"

txt_template = 'This is my HTML template for Booking service'
msg_root = "Welcome to the Booking service!"
msg_booking_user_not_found = "booking user not found"
msg_user_id_not_found = "User ID not found"
msg_movie_id_not_found = "movie ID not found"


#  ------ Uploads ------

with open('bookings.json'.format("."), "r") as jsf:
    db_JSON = json.load(jsf)
# DB
bookings = db_JSON["bookings"]

# ----- Functions for API requests ------


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


@app.route("/bookings", methods=['GET'])
def get_json():
    """ Get the complete Booking JSON file or a booking for a given user ID

    Parameters:
        userid (string): user booking ID

    Returns:
        - message: Error message if user ID doesn't exists
        - JSON: The booking details which correspond to the 
                user ID in JSON format
        - JSON: Bookings in JSON format
    """
    # Case : user id is pass in parameters
    if request.args:
        list_bookings_by_user = []
        req = request.args
        for booking in bookings:
            if str(booking["userid"]) == str(req["userid"]):
                list_bookings_by_user.append(booking)
        if not list_bookings_by_user:
            res = make_response(
                jsonify({"error": msg_booking_user_not_found}), 400)
            return res
        res = make_response(jsonify(list_bookings_by_user), 200)
        return res

    # Case : there is no parameters
    return make_response(jsonify(db_JSON), 200)


@app.route("/bookings/<userid>", methods=["POST"])
def create_booking(userid):
    """ Add a new booking to a given user ID

    Args:
        userid (string): The user ID for which you must add a new booking

    Returns:
        - JSON: Added booking in JSON format
        - message: Error message if user ID not found 

    Example:
        JSON:
            {
                "dates": [
                    {
                    "date": "20151201",
                    "movies": [
                        "267eedb8-0f5d-42d5-8f43-72426b9fb3e6",
                        "7daf7208-be4d-4944-a3ae-c1c2f516f3e6",
                        "39ab85e5-5e8e-4dc5-afea-65dc368bd7ab",
                        "a8034f44-aee4-44cf-b32c$$$$$$"
                        ]
                    },
                    {
                    "date": "20151204",
                    "movies": [
                        "96798c08-d19b-4986-a05d-7da856efb697"
                        ]
                    }
                ]
            }
    """
    req = request.get_json()
    for booking in bookings:

        if str(booking["userid"]) == str(userid):

            for date in req["dates"]:  # Iterate through all the new date to add

                booking["dates"].append(
                    {"date": "", "movies": []})  # Create a new date
                avalable_movie = get_movie_by_date(str(date["date"]))

                # Iterate through all the existing date
                for items in booking["dates"]:
                    if not items["date"]:  # Verfy if date is empty in order to add

                        for movie in date["movies"]:

                            if movie in avalable_movie:  # Verify if movie is avalable on give date throw Time API

                                items["date"] = date["date"]
                                items["movies"].append(movie)

            return make_response(jsonify(booking), 400)

    res = make_response(jsonify({"Error": msg_user_id_not_found}), 200)
    return res


@app.route("/bookings/<userid>", methods=["DELETE"])
def del_movie(userid):
    """ Dellete a booking from a given user id

    Args:
        userid (string): User ID to delete booking

    Returns:
        - JSON: Deleted booking details in JSON format
        - message: Error message if user ID is not found
    """
    deleted_bookings = []
    for booking in bookings:
        if str(booking["userid"]) == str(userid):
            bookings.remove(booking)
            deleted_bookings.append(booking)
            return make_response(jsonify(bookingDelete), 200)

    res = make_response(jsonify({"error": msg_user_id_not_found}), 400)
    return res

# Ex : bookings/schedule/20151130


def get_movie_by_date(date):
    """ Get movie(s) id(s) with a given date / avalables movies on a given date

    Args:
        date (string): the date to search for a movie

    Returns:
        JSON: Movie id's JSON format list
    """
    parameters = {
        "date": str(date)
    }
    response = requests.get(
        TIME_API_URL, params=parameters)
    return response.json()

# Main function to launch Booking API/App


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)

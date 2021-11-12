# ------ Imports -------

from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

# ------ Constants -------

app = Flask(__name__)

PORT = 3500
HOST = 'localhost'

txt_template = 'This is my HTML template for Booking service'
msg_root = "This is my HTML template for Time service"

#  ------ Uploads ------

with open('times.json'.format("."), "r") as jsf:
    db_JSON = json.load(jsf)

schedules = db_JSON["schedule"]

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


@app.route("/showtimes", methods=['GET'])
def get_json():
    """Get the complete Time JSON file

    Returns:
        JSON: Schedules in JSON format
    """
    res = make_response(jsonify(db_JSON), 200)
    return res


# TODO Add ecemple in doc/comments : Ex: /showmovies?date=20151130


@app.route("/showmovies", methods=['GET'])
def get_movietime_by_date():
    """ Get a movie(s) with a given date

    Parameters:
        date (string): date to find a movie

    Returns:
        - message: Error message if no movie is found for the given date
        - JSON: Movie id list in JSON format
    """
    list_movies_by_date = []
    if request.args:
        req = request.args
        for schedule in schedules:
            if int(schedule["date"]) == int(req["date"]):
                list_movies_by_date.append(schedule)

    if not list_movies_by_date:
        res = make_response(
            jsonify({"Empty": "There is no movie for the given date"}), 400)
        return res
    res = make_response(jsonify(list_movies_by_date[0]["movies"]), 200)
    return res

# Main function to launch Time API/App


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
    # app.run()

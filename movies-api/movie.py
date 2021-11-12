# ------ Imports -------

from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

# ------ Constants -------

app = Flask(__name__)

PORT = 3200
HOST = 'localhost'

txt_template = 'This is my HTML template for Booking service'
msg_root = "<h1 style='color:blue'>Welcome to the Movie service!</h1>"
msg_movie_id_not_found = "movie ID not found"
msg_movie_id_exists = "movie ID already exists"
msg_movie_title_error = "movie title not found"
msg_movie_price = "movie price not found"

#  ------ Uploads ------

with open('.\movies.json'.format("."), "r") as jsf:
    db_JSON = json.load(jsf)

movies = db_JSON["movies"]
links = db_JSON["links"]

# TODO: Add in comment/doc function example of a "requête"

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


@app.route("/json", methods=['GET'])
def get_json():
    """Get the complete Movies JSON file

    Returns:
        JSON: Movies in JSON format
    """
    res = make_response(jsonify(db_JSON), 200)
    return res


@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    """Get a movie infos/details by its ID

    Args:
        movieid (string): existing movie ID

    Returns:
        JSON: A movie details in JSON format 
    """
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify(movie), 200)
            return res
    return make_response(jsonify({"error": msg_movie_id_not_found}), 400)


@app.route("/movies/<movieid>", methods=["POST"])
def create_movie(movieid):
    """Add a new movie to the DB

    Args:
        movieid (string): new movie ID

    Returns:
        - message: Error message if moive ID already exists
        - JSON: Added movie details in JSON format
    """
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error": msg_movie_id_exists}), 409)

    movies.append(req)
    res = make_response(jsonify({"message": "movie added"}), 200)
    return res


@app.route("/movies/<movieid>", methods=["DELETE"])
def del_movie(movieid):
    """Delete a movie from a given ID

    Args:
        movieid (string): ID of the movie to delete

    Returns:
        - JSON: Deleted movie details in JSON format
        - message: Error message if moive ID doesn't exists
    """
    movie_delete = []
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            movie.pop("links")
            movie_delete.append(movie)
            movie_delete.append(links)
            return make_response(jsonify(movieDelete), 200)

    res = make_response(jsonify({"error": msg_movie_id_not_found}), 400)
    return res


@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    """Get movie details by title

    Parameters:
        titile (string): Movie title

    Returns:
        - JSON: Movie details in JSON format
        - message: Error message if moive title not found
    """
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                return make_response(jsonify(movie), 200)

    return make_response(jsonify({"error": msg_movie_title_error}), 400)


@app.route("/movies/<movieid>/<rate>", methods=["PUT"])
def update_movie_rating(movieid, rate):
    """ Update movie rating

    Args:
        movieid (string): Movie ID for which to update rateing
        rate (float): new rating

    Returns:
        - JSON: Movie details in JSON format with rating updated
        - message: Error message if movie id is invalid
    """
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = int(rate)
            res = make_response(jsonify(movie), 200)
            return res

    res = make_response(jsonify({"error": msg_movie_id_not_found}), 201)
    return res


@app.route("/moviesbydirector", methods=['GET'])
def get_movie_bydirector():
    """Get a movie details by its director

    Parameters:
        director (string): Movie director

    Returns:
        - JSON: Movie details in JSON format
        - message: Error message if director not found 
    """
    list_directors = []
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["director"]).split() == str(req["director"]).split():
                list_directors.append(movie)

    if not list_directors:
        res = make_response(jsonify({"error": "director not found"}), 400)
        return res
    res = make_response(jsonify(list_directors), 200)
    return res


@app.route("/moviesbyprice", methods=['GET'])
def get_movie_byprice():
    """ Get a movie according to a price

    Parameters:
        price (int): Movie price

    Returns:
        - JSON: Movie details in JSON format
        - message: Error message if no movie is found for the given price
    """
    list_price = []
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["price"]) == str(req["price"]):
                list_price.append(movie)

    if not list_price:
        res = make_response(jsonify({"error": msg_movie_price}), 400)
        return res
    res = make_response(jsonify(list_price), 200)
    return res


@app.route("/moviesprice/<movieid>/<price>", methods=["PUT"])
def update_movie_price(movieid, price):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["price"] = int(price)
            res = make_response(jsonify(movie), 200)
            return res

    res = make_response(jsonify({"error": msg_movie_id_not_found}), 201)
    return res

# Main function to launch Movie API/App


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)

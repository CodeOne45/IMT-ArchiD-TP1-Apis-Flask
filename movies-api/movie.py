from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = '192.168.0.15'

with open('.\movies.json'.format("."), "r") as jsf:
   db_JSON = json.load(jsf)

movies = db_JSON["movies"]
links = db_JSON["links"]


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",  200)

# to test templates of Flask
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for Movie service'),200)

# get the complete json file
@app.route("/json", methods=['GET'])
def get_json():
    #res = make_response(jsonify(INFO), 200)

    res =  make_response(jsonify(db_JSON), 200)
    res = res
    return res

# get a movie info by its ID
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    for movie in movies:        
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify(movie),200)
            return res
    return make_response(jsonify({"error":"Movie ID not found"}),400)
    
# add a new movie
@app.route("/movies/<movieid>", methods=["POST"])
def create_movie(movieid):
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error":"movie ID already exists"}),409)

    movies.append(req)
    res = make_response(jsonify({"message":"movie added"}),200)
    return res

# delete a movie
@app.route("/movies/<movieid>", methods=["DELETE"])
def del_movie(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify(movie),200)

    res = make_response(jsonify({"error":"movie ID not found"}),400)
    return res

# get a movie info by its name
# through a query
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    json = ""
    if request.args:
        req = request.args
        for movie in movies:        
            if str(movie["title"]) == str(req["title"]):
                json = movie
                
    if not json:
        res = make_response(jsonify({"error":"movie title not found"}),400)
    else:
        res = make_response(jsonify(json),200)
    return res

# change a movie rating
@app.route("/movies/<movieid>/<rate>", methods=["PUT"])
def update_movie_rating(movieid, rate):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = int(rate)
            res = make_response(jsonify(movie),200)
            return res

    res = make_response(jsonify({"error":"movie ID not found"}),201)
    return res

#get a movie info by its director
@app.route("/moviesbydirector", methods=['GET'])
def get_movie_bydirector():
    listDirector = []
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["director"]).split() == str(req["director"]).split():
                listDirector.append(movie)
                
    if not listDirector:
        res = make_response(jsonify({"error": "director not found"}),400)
        return res
    res = make_response(jsonify(listDirector),200)
    return res


# get a movie by its price
# through a query
@app.route("/moviesbyprice", methods=['GET'])
def get_movie_byprice():
    listPrice = []
    if request.args:
        req = request.args
        for movie in movies:        
            if str(movie["price"]) == str(req["price"]):
                    listPrice.append(movie)
                
    if not listPrice:
        res = make_response(jsonify({"error":"movie price not found"}),400)
        return res    
    res = make_response(jsonify(listPrice),200)
    return res
# change a movie price
@app.route("/moviesprice/<movieid>/<price>", methods=["PUT"])
def update_movie_price(movieid, price):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["price"] = int(price)
            res = make_response(jsonify(movie),200)
            return res

    res = make_response(jsonify({"error":"movie ID not found"}),201)
    return res

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
   # app.run(host=HOST, port=PORT)
    app.run()
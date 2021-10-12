from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3500
HOST = '192.168.0.15'

with open('times.json'.format("."), "r") as jsf:
   db_JSON = json.load(jsf)

schedules = db_JSON["schedule"]
#links = db_JSON["links"]


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Time service!</h1>",  200)

# to test templates of Flask
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for Time service'),200)

# get the complete json database
@app.route("/showtimes", methods=['GET'])
def get_json():
    res =  make_response(jsonify(db_JSON), 200)
    res = res
    return res

# get a movie(d) by its date
# through a query
@app.route("/showmovies", methods=['GET'])
def get_movieTime_bydate():
    listMoviesByDate = []
    if request.args:
        req = request.args
        for schedule in schedules:        
            if int(schedule["date"]) == int(req["date"]):
                    listMoviesByDate.append(schedule)
                
    if not listMoviesByDate:
        res = make_response(jsonify({"error":"movie date not found"}),400)
        return res    
    res = make_response(jsonify(listMoviesByDate),200)
    return res


if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    #app.run(host=HOST, port=PORT)
    app.run()
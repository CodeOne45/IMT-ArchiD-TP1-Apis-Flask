import json
import grpc
from concurrent import futures
import movie_pb2
import movie_pb2_grpc


class MovieServicer(movie_pb2_grpc.MovieServicer):
    def __init__(self):
        with open('./databases/movies.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]

    def AddMovie(self, request, context):
        for movie in self.db:
            if movie["id"] == request.id:
                print("Error : Movie ID already exist !")
                return movie_pb2.MovieData(title="", rating=0.0, director="", id="")
        newMovie = {
            "title": request.title,
            "rating": request.rating,
            "director": request.director,
            "id": request.id
        }
        self.db.append(newMovie)
        return request

    def DeleteMovie(self, request, context):
        for movie in self.db:
            if movie["id"] == request.id:
                print("Movie delete !")
                deletedMovie = movie_pb2.MovieData(
                    title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
                self.db.remove(movie)
                return deletedMovie

        print("Movie not exist !")
        return movie_pb2.MovieData(title="", rating=0.0, director="", id="")

    def UpdateMovieRate(self, request, context):
        for movie in self.db:
            if movie["id"] == request.id:
                movie["rating"] = request.rating
                print("Movie updated !")
                return movie_pb2.Empty()

        print("Movie ID not exist !")
        return movie_pb2.Empty()

    def GetMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found!")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData(title="", rating=0.0, director="", id="")

    def GetListMovies(self, request, context):
        for movie in self.db:
            yield movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])

    def GetMovieByDirector(self, request, context):
        for movie in self.db:
            if movie['director'] == request.director:
                print("Movie found for the given director !")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData(title="", rating=0.0, director="", id="")

    def GetMovieByTitle(self, request, context):
        for movie in self.db:
            if movie['title'] == request.title:
                print("Movie found")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData(title="", rating=0.0, director="", id="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

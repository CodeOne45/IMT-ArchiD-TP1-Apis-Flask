import grpc
import movie_pb2
import movie_pb2_grpc


def addMovie(stub, MovieData):
    newMovie = stub.AddMovie(MovieData)
    print(newMovie)


def deleteMovie(stub, id):
    movie = stub.DeleteMovie(id)
    print(movie)


def updateMovieRate(stub, rating):
    updatedMovie = stub.UpdateMovieRate(rating)
    print(updatedMovie)


def get_movie_by_id(stub, id):
    movie = stub.GetMovieByID(id)
    print(movie)


def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))


def run():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        print("-------------- AddNewMovie --------------")
        new_movie = movie_pb2.MovieData(
            title="testMovie", rating=2.6, director="Theo", id="a564e654f5ef5ef5e4f-dvd-dvdv-ddnhykuy67v")
        addMovie(stub, new_movie)

        print("-------------- DeleteMovieByID --------------")
        deleteMovieId = movie_pb2.MovieID(
            id="39ab85e5-5e8e-4dc5-afea-65dc368bd7ab")
        deleteMovie(stub, deleteMovieId)

        print("-------------- UpdateMovieRate --------------")
        rate = movie_pb2.Rate(
            rating=2.3, id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        updateMovieRate(stub, rate)

        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)

        print("-------------- GetListMovies --------------")
        get_list_movies(stub)


if __name__ == '__main__':
    run()

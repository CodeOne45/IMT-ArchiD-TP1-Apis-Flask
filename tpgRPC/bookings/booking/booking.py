import json
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('./database/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def CreatBooking(self, request, context):
        return TODO

    def DeleteBooking(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.userid:
                print("Booking delete !")
                deletedBooking = booking_pb2.BookingData(userid=booking["userid"], date=booking_pb2.DatesMovies(
                    date=booking["dates"][0]["date"], movies=booking["dates"][0]["movies"]))

                self.db.remove(booking)
                return deletedBooking

        print("Movie not exist !")
        return movie_pb2.MovieData(title="", rating=0.0, director="", id="")

    def GetListBookings(self, request, context):
        for booking in self.db:
            for date in booking["dates"]:
                print(date["date"])
                yield booking_pb2.BookingData(userid=booking["userid"], dates=booking_pb2.DatesMovies(date=date["date"], movies=date["movies"]))

    def GetBookingByUserID(self, request, context):
        return TODO

    def GetMovieByTime(self, request, context):
        return TODO


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(
        BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

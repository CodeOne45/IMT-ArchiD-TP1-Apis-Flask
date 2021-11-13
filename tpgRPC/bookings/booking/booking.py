import json
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('./database/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def CreatBooking(self, request, context):
        newBooking = {}
        newBooking['userid'] = request.userid
        newBooking['dates'] = []

        for date in request.dates:  # Create new dates type's according to nb of dates to add
            newBooking['dates'].append({"date": "", "movies": []})

        with grpc.insecure_channel('localhost:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            # Iteration on nb of date to add
            for i in range(len(newBooking['dates'])):
                answer = stub.Getshowmovies(
                    booking_pb2.Date(date=request.dates[i].date))  # Connection to Time API
                for booking in self.db:
                    if booking["userid"] == request.userid:
                        # Iteration on nb of movie to add in the date of previous "for" loop
                        for movie in request.dates[i].movies:
                            print(answer.idMovies)
                            if str(movie) in answer.idMovies:
                                print(
                                    "Movie avalable for the given date !" + str(movie))
                                # Add date to new dates
                                newBooking['dates'][i]['date'] = request.dates[i].date
                                newBooking['dates'][i]['movies'].append(
                                    movie)  # Add movie to new movies
                                print(newBooking['dates'][i])
                            else:
                                print(
                                    "Movie not avalable for the given date !")

        self.db.append(newBooking)
        return booking_pb2.BookingData(userid=newBooking["userid"], dates=newBooking["dates"])

    def DeleteBooking(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.userid:
                print("Booking deleted !")
                deletedBooking = booking_pb2.BookingData(
                    userid=booking["userid"], dates=booking["dates"])
                self.db.remove(booking)
                return deletedBooking

        print("Booking not exist !")
        return booking_pb2.BookingData(userid="", dates="")

    def GetListBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingData(userid=booking["userid"], dates=booking["dates"])

    def GetBookingByUserID(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.userid:
                print("Booking found!")
                for date in booking['dates']:
                    for movie in date['movies']:
                        yield booking_pb2.SingleBookingData(userid=booking['userid'], date=date['date'], movies=movie)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(
        BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

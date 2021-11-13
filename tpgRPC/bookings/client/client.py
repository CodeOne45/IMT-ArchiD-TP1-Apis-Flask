import grpc
import booking_pb2
import booking_pb2_grpc


def get_list_bookings(stub):
    allBookings = stub.GetListBookings(booking_pb2.Empty())
    tmp = 1
    for booking in allBookings:
        print("Booking n° %d %s" % (tmp, booking))
        tmp = tmp + 1


def add_booking(stub, newBooking):
    reponse = stub.CreatBooking(newBooking)
    print(reponse)


def delete_bookings(stub, userid):
    booking = stub.DeleteBooking(userid)
    print(booking)


def get_booking_by_user(stub, userid):
    bookings = stub.GetBookingByUserID(userid)
    for booking in bookings:
        print(booking)


def run():
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)

        print("-------------- GetListBookings --------------")
        get_list_bookings(stub)

        print("---------------- AddBooking --------------")
        newBooking = booking_pb2.BookingData(userid="chris_rivers", dates=[booking_pb2.DatesMovies(
            date="20151130", movies=["720d006c-3a57-4b6a-b18f-9b713b073f3c", "a8034f44-aee4-44cf-b32c-74cf452aaaae"]), booking_pb2.DatesMovies(
            date="20151201", movies=["267eedb8-0f5d-42d5-8f43-72426b9fb3e6", "54sds54c466s4s84s4d65s"])])
        add_booking(stub, newBooking)

        print("---------------- DeleteBooking --------------")
        deleteBooking = booking_pb2.UserID(userid="chris_rivers")
        delete_bookings(stub, deleteBooking)

        print("---------------- Get Booking by User ---------")
        bookingByUser = booking_pb2.UserID(userid="garret_heaton")
        get_booking_by_user(stub, bookingByUser)


if __name__ == '__main__':
    run()

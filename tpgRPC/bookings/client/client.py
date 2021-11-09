import grpc
import booking_pb2
import booking_pb2_grpc


def get_list_bookings(stub):
    allBookings = stub.GetListBookings(booking_pb2.Empty())
    tmp = 1
    for booking in allBookings:
        print("Booking %d %s" % (tmp, booking))
        tmp = tmp + 1


def run():
    with grpc.insecure_channel('localhost:3002') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)

        print("-------------- GetListMovies --------------")
        get_list_bookings(stub)


if __name__ == '__main__':
    run()

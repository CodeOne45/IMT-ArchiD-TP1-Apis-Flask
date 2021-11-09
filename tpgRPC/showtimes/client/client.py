import grpc
import showtime_pb2_grpc
import showtime_pb2


def get_showtimes_by_date(stub, date):
    showtime = stub.Getshowmovies(date)
    print(showtime)


def get_list_showtimes(stub):
    allshowtimes = stub.GetListShowtimes(showtime_pb2.Empty())
    for showtime in allshowtimes:
        print("Showtime date %s" % (showtime))


def run():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetShowtimebyDate --------------")
        showtimeDate = showtime_pb2.Date(date="24042001")
        get_showtimes_by_date(stub, showtimeDate)

        print("-------------- GetListShowtimes --------------")
        get_list_showtimes(stub)


if __name__ == '__main__':
    run()

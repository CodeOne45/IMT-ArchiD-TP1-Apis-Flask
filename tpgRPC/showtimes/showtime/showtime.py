import json
import grpc
from concurrent import futures
import showtime_pb2_grpc
import showtime_pb2


class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):
    def __init__(self):
        with open('./database/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    def Getshowmovies(self, request, context):
        for showtime in self.db:
            if showtime['date'] == request.date:
                print("showtime found!")
                return showtime_pb2.ShowTimeData(date=showtime["date"], idMovies=showtime["movies"])

        return showtime_pb2.ShowTimeData(date="", idMovies="")

    def GetListShowtimes(self, request, context):
        for showtime in self.db:
            yield showtime_pb2.ShowTimeData(date=showtime["date"], idMovies=showtime["movies"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(
        ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

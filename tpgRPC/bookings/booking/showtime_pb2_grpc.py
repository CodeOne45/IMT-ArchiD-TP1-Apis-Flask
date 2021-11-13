# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2
import showtime_pb2 as showtime__pb2


class ShowtimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Getshowmovies = channel.unary_unary(
                '/Showtime/Getshowmovies',
                request_serializer=booking__pb2.Date.SerializeToString,
                response_deserializer=showtime__pb2.ShowTimeData.FromString,
                )
        self.GetListShowtimes = channel.unary_stream(
                '/Showtime/GetListShowtimes',
                request_serializer=booking__pb2.Empty.SerializeToString,
                response_deserializer=showtime__pb2.ShowTimeData.FromString,
                )


class ShowtimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Getshowmovies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListShowtimes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShowtimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Getshowmovies': grpc.unary_unary_rpc_method_handler(
                    servicer.Getshowmovies,
                    request_deserializer=booking__pb2.Date.FromString,
                    response_serializer=showtime__pb2.ShowTimeData.SerializeToString,
            ),
            'GetListShowtimes': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListShowtimes,
                    request_deserializer=booking__pb2.Empty.FromString,
                    response_serializer=showtime__pb2.ShowTimeData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Showtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Showtime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Getshowmovies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Showtime/Getshowmovies',
            booking__pb2.Date.SerializeToString,
            showtime__pb2.ShowTimeData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListShowtimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Showtime/GetListShowtimes',
            booking__pb2.Empty.SerializeToString,
            showtime__pb2.ShowTimeData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

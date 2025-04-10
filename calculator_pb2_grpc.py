# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SquareRoot = channel.unary_unary(
                '/calculator.Calculator/SquareRoot',
                request_serializer=calculator__pb2.Number.SerializeToString,
                response_deserializer=calculator__pb2.Number.FromString,
                )
        self.Add = channel.unary_unary(
                '/calculator.Calculator/Add',
                request_serializer=calculator__pb2.NumberPair.SerializeToString,
                response_deserializer=calculator__pb2.Number.FromString,
                )
        self.Subtract = channel.unary_unary(
                '/calculator.Calculator/Subtract',
                request_serializer=calculator__pb2.NumberPair.SerializeToString,
                response_deserializer=calculator__pb2.Number.FromString,
                )
        self.Multiply = channel.unary_unary(
                '/calculator.Calculator/Multiply',
                request_serializer=calculator__pb2.NumberPair.SerializeToString,
                response_deserializer=calculator__pb2.Number.FromString,
                )
        self.Divide = channel.unary_unary(
                '/calculator.Calculator/Divide',
                request_serializer=calculator__pb2.NumberPair.SerializeToString,
                response_deserializer=calculator__pb2.Number.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SquareRoot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subtract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Multiply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Divide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SquareRoot': grpc.unary_unary_rpc_method_handler(
                    servicer.SquareRoot,
                    request_deserializer=calculator__pb2.Number.FromString,
                    response_serializer=calculator__pb2.Number.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=calculator__pb2.NumberPair.FromString,
                    response_serializer=calculator__pb2.Number.SerializeToString,
            ),
            'Subtract': grpc.unary_unary_rpc_method_handler(
                    servicer.Subtract,
                    request_deserializer=calculator__pb2.NumberPair.FromString,
                    response_serializer=calculator__pb2.Number.SerializeToString,
            ),
            'Multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiply,
                    request_deserializer=calculator__pb2.NumberPair.FromString,
                    response_serializer=calculator__pb2.Number.SerializeToString,
            ),
            'Divide': grpc.unary_unary_rpc_method_handler(
                    servicer.Divide,
                    request_deserializer=calculator__pb2.NumberPair.FromString,
                    response_serializer=calculator__pb2.Number.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculator.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SquareRoot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/SquareRoot',
            calculator__pb2.Number.SerializeToString,
            calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/Add',
            calculator__pb2.NumberPair.SerializeToString,
            calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subtract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/Subtract',
            calculator__pb2.NumberPair.SerializeToString,
            calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/Multiply',
            calculator__pb2.NumberPair.SerializeToString,
            calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Divide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/Divide',
            calculator__pb2.NumberPair.SerializeToString,
            calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

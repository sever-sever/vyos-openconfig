# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vyos.protos import vyos_pb2 as vyos_dot_protos_dot_vyos__pb2


class VyosConfigServiceStub(object):
    """VyosConfigService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetConfig = channel.unary_unary(
                '/VyosConfigService/SetConfig',
                request_serializer=vyos_dot_protos_dot_vyos__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=vyos_dot_protos_dot_vyos__pb2.SetConfigReply.FromString,
                )
        self.GetConfig = channel.unary_unary(
                '/VyosConfigService/GetConfig',
                request_serializer=vyos_dot_protos_dot_vyos__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=vyos_dot_protos_dot_vyos__pb2.GetConfigReply.FromString,
                )
        self.GetCounters = channel.unary_unary(
                '/VyosConfigService/GetCounters',
                request_serializer=vyos_dot_protos_dot_vyos__pb2.RxpacketRequest.SerializeToString,
                response_deserializer=vyos_dot_protos_dot_vyos__pb2.RxpacketReply.FromString,
                )
        self.GetCountersStream = channel.unary_stream(
                '/VyosConfigService/GetCountersStream',
                request_serializer=vyos_dot_protos_dot_vyos__pb2.RxpacketRequest.SerializeToString,
                response_deserializer=vyos_dot_protos_dot_vyos__pb2.RxpacketReply.FromString,
                )


class VyosConfigServiceServicer(object):
    """VyosConfigService
    """

    def SetConfig(self, request, context):
        """Set VyOS configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfig(self, request, context):
        """Get VyOS configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCounters(self, request, context):
        """Get RX packets Counter
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCountersStream(self, request, context):
        """Get RX packets Counter stream
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VyosConfigServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=vyos_dot_protos_dot_vyos__pb2.SetConfigRequest.FromString,
                    response_serializer=vyos_dot_protos_dot_vyos__pb2.SetConfigReply.SerializeToString,
            ),
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=vyos_dot_protos_dot_vyos__pb2.GetConfigRequest.FromString,
                    response_serializer=vyos_dot_protos_dot_vyos__pb2.GetConfigReply.SerializeToString,
            ),
            'GetCounters': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCounters,
                    request_deserializer=vyos_dot_protos_dot_vyos__pb2.RxpacketRequest.FromString,
                    response_serializer=vyos_dot_protos_dot_vyos__pb2.RxpacketReply.SerializeToString,
            ),
            'GetCountersStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCountersStream,
                    request_deserializer=vyos_dot_protos_dot_vyos__pb2.RxpacketRequest.FromString,
                    response_serializer=vyos_dot_protos_dot_vyos__pb2.RxpacketReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VyosConfigService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VyosConfigService(object):
    """VyosConfigService
    """

    @staticmethod
    def SetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VyosConfigService/SetConfig',
            vyos_dot_protos_dot_vyos__pb2.SetConfigRequest.SerializeToString,
            vyos_dot_protos_dot_vyos__pb2.SetConfigReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VyosConfigService/GetConfig',
            vyos_dot_protos_dot_vyos__pb2.GetConfigRequest.SerializeToString,
            vyos_dot_protos_dot_vyos__pb2.GetConfigReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCounters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VyosConfigService/GetCounters',
            vyos_dot_protos_dot_vyos__pb2.RxpacketRequest.SerializeToString,
            vyos_dot_protos_dot_vyos__pb2.RxpacketReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCountersStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/VyosConfigService/GetCountersStream',
            vyos_dot_protos_dot_vyos__pb2.RxpacketRequest.SerializeToString,
            vyos_dot_protos_dot_vyos__pb2.RxpacketReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

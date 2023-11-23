#!/usr/bin/env python3

"""
Script: node_grpc_server.py
Author: Viacheslav Hletenko
Date: 2023
Descritpion: gRPC server script
"""

import json
import time
from concurrent import futures

import grpc

from vyos.protos import (
    # Base classes
    vyos_pb2,
    vyos_pb2_grpc
)
from vyos.utils import rc_cmd


def get_rx_packets(interface):
    rc, out = rc_cmd(f'ip -s -j link show {interface}')
    if rc == 0:
        interface_info = json.loads(out)[0]
        return interface_info['stats64']['rx']['packets']
    return 0


class VyosConfigServiceServicer(vyos_pb2_grpc.VyosConfigServiceServicer):

    def SetConfig(self, request, context):
        return vyos_pb2.SetConfigReply(
            message='Configuration set successfully')

    def GetConfig(self, request, context):
        config = 'Sample VyOS configuration'
        return vyos_pb2.GetConfigReply(config=config)

    def GetCounters(self, request, context):
        """Get interface RX counters"""
        rx_packets = get_rx_packets(request.interface)
        return vyos_pb2.RxpacketReply(
            message=f'Rx packets for {request.interface}: {rx_packets}')

    def GetCountersStream(self, request, context):
        """Get interface RX counters stream"""
        while True:
            rx_packets = get_rx_packets(request.interface)
            yield vyos_pb2.RxpacketReply(
                message=f'Rx packets for {request.interface}: {rx_packets}')
            time.sleep(1)


def serve():
    # gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vyos_pb2_grpc.add_VyosConfigServiceServicer_to_server(
        VyosConfigServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

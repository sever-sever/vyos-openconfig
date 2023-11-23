#!/usr/bin/env python3

"""
Script: client.py
Author: Viacheslav Hletenko
Date: 2023
Descritpion: gRPC client
"""

import grpc

from vyos.protos import (
    # Base classes
    vyos_pb2,
    vyos_pb2_grpc
)


def main():
    # Create gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = vyos_pb2_grpc.VyosConfigServiceStub(channel)

    # Set configuration
    response = stub.SetConfig(
        vyos_pb2.SetConfigRequest(config='my_configuration'))
    print('SetConfig response:', response.message)

    # Get configuration
    response = stub.GetConfig(vyos_pb2.GetConfigRequest())
    print('GetConfig response:', response.config)

    # Get interface RX counters
    response = stub.GetCounters(vyos_pb2.RxpacketRequest(interface='enp8s0'))
    print(f'GetCounters: {response}')
    # print('GetCounter response:', response.rxpackets)


if __name__ == '__main__':
    main()

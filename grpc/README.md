# gRPC

Required packages `grpcio` and `grpcio-tools`
```shell
pip3 install grpcio==1.59.3 grpcio-tools==1.59.3
```

Generate protos
```shell
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. vyos/protos/vyos.proto
```

Start gRPC server:
```shell
./node_grpc_server.py
```

Start gRCP client:
```
$ ./client.py 
SetConfig response: Configuration set successfully
GetConfig response: Sample VyOS configuration
GetCounters: message: "Rx packets for enp8s0: 732634"

```

Additional links
[proto3](https://protobuf.dev/programming-guides/proto3/) and [quickstart](https://grpc.io/docs/languages/python/quickstart/)
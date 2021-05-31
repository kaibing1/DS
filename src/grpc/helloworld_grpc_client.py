#!  /Users/mr.yang/anaconda3/bin/python
# -*- coding: utf-8 -*-

"""
    created on 
    
    @author: Mr.Yang
"""
import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")

    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name="lz"))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name="again"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    run()
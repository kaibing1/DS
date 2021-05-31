#!  /Users/mr.yang/anaconda3/bin/python
# -*- coding: utf-8 -*-

"""
    created on 
    
    @author: Mr.Yang
"""
import grpc
import task_pb2
import task_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")

    stub = task_pb2_grpc.TaskStub(channel)
    response = stub.Take(task_pb2.HelloRequest(name="wo"))

    print("Greeter client received: " + response.message)

    response = stub.Handle(task_pb2.HelloRequest(name="wo"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    run()
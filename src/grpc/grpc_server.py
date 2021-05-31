#!  /Users/mr.yang/anaconda3/bin/python
# -*- coding: utf-8 -*-

"""
    created on 
    
    @author: Mr.Yang
"""
from concurrent import futures
import time
import grpc
import task_pb2
import task_pb2_grpc
import random


class Greeter(task_pb2_grpc.TaskServicer):
    def __init__(self):
        self.map = {}

    def Take(self, request, context):
        msg = request.name
        if msg not in self.map.keys():
            self.map[msg] = random.randint(1, 10)
        return task_pb2.HelloReply(message = 'task id: {msg}'.format(msg=self.map.get(msg)))

    def Handle(self, request, context):

        return task_pb2.HelloReply(message = 'finish {msg}'.format(msg=self.map.get(request.name)))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()

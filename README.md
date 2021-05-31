# DS

### 编译 proto

``` console
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. helloworld.proto
```
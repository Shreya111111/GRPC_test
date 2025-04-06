# gRPC in Python


```shell
git clone https://github.com/ramananbalakrishnan/basic-grpc-python
cd basic-grpc-python
pip install -r requirements.txt
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
python server.py
python client.py
```


import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc
import calculator

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

    def Add(self, request, context):
        return calculator_pb2.Number(value=calculator.add(request.a, request.b))

    def Subtract(self, request, context):
        return calculator_pb2.Number(value=calculator.subtract(request.a, request.b))

    def Multiply(self, request, context):
        return calculator_pb2.Number(value=calculator.multiply(request.a, request.b))

    def Divide(self, request, context):
        try:
            result = calculator.divide(request.a, request.b)
            return calculator_pb2.Number(value=result)
        except ValueError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
            return calculator_pb2.Number()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("✅ Calculator Server running at port 50051")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

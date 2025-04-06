import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Square Root
    number = calculator_pb2.Number(value=16)
    response = stub.SquareRoot(number)
    print(f"√16 = {response.value}")

    # Add
    pair = calculator_pb2.NumberPair(a=10, b=5)
    print(f"10 + 5 = {stub.Add(pair).value}")

    # Subtract
    print(f"10 - 5 = {stub.Subtract(pair).value}")

    # Multiply
    print(f"10 * 5 = {stub.Multiply(pair).value}")

    # Divide
    print(f"10 / 5 = {stub.Divide(pair).value}")

if __name__ == '__main__':
    run()

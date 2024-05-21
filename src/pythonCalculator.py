from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def basicCalculator(operation, num1, num2):
    result = 0

    match operation:
        #if operation = ADD, return the sum
        case Operation.ADD:
            print("")
        case Operation.SUBTRACT:
            print("")
        case Operation.MULTIPLY:
            print("")
        case Operation.DIVIDE:
            if num2 == 0:
                print("")
            else:
                result = num1 / num2
    return result


if __name__ == "__main__":
    print(basicCalculator(Operation.DIVIDE, 1, 2))


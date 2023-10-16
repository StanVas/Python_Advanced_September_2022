def operate(*args):
    def add():
        result = 0
        for num in args[1:]:
            result += num
        return result

    def subtract():
        result = 0
        for num in args[1:]:
            result -= num
        return result

    def multiply():
        result = 1
        for num in args[1:]:
            result *= num
        return result

    def divide():
        result = args[1]
        for num in args[2:]:
            result /= num
        return result

    operator = args[0]
    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("-", 1, 2, 3))
print(operate("/", 3, 4))
print(operate("+", 3, 4))
print(operate("*", 3, 4))

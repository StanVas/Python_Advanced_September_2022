def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def pow_raise(a, b):
    return a ** b


def calculate(a, b, op):
    if op == '/':
        return divide(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '^':
        return pow_raise(a, b)

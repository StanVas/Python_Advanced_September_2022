from utils.math_oper import calculate

math_sequence = input().split()

num1 = float(math_sequence[0])
operator = math_sequence[1]
num2 = float(math_sequence[2])

result = calculate(num1, num2, operator)

print(f'{result:.2f}')

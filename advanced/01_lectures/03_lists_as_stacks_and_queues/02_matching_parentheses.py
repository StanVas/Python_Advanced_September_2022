expression = input()
stack = []

for idx in range(len(expression)):
    ch = expression[idx]
    if ch == '(':
        stack.append(idx)

    elif ch == ')':
        start_idx = stack.pop()
        sub_expression = expression[start_idx:idx + 1]
        print(sub_expression)

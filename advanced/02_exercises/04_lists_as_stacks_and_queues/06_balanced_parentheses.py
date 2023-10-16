parentheses = input()
result = True
opening_stack = []


for el in parentheses:
    if el in '([{':
        opening_stack.append(el)
    elif el == ')':
        if opening_stack and opening_stack[-1] == '(':
            opening_stack.pop()
        else:
            result = False
            break
    elif el == '}':
        if opening_stack and opening_stack[-1] == '{':
            opening_stack.pop()
        else:
            result = False
            break
    elif el == ']':
        if opening_stack and opening_stack[-1] == '[':
            opening_stack.pop()
        else:
            result = False
            break

print('YES' if result else 'NO')

stack = []
actions = int(input())

for _ in range(actions):
    action = input().split()
    type = action[0]
    if type == '1':
        number = action[1]
        stack.append(number)
    elif type == '2':
        if stack:
            stack.pop()
    elif type == '3':
        if stack:
            print(max(stack, key=int))
    elif type == '4':
        if stack:
            print(min(stack, key=int))

print_stack = []
while stack:
    print_num = stack.pop()
    print_stack.append(print_num)

print(', '.join(print_stack))

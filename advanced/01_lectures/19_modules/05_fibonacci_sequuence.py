from utils.fibinacci import locate, create, parse_line

nums = []
while True:
    command = input()
    if command == "Stop":
        break
    action, arg = parse_line(command)

    if action == 'Create':
        nums = create(arg)
        print(*create(arg))

    elif action == 'Locate':
        idx = locate(arg, nums)
        output = f'The number {arg} is not in the sequence' if idx == -1 else f'The number - {arg} is at index {idx}'
        print(output)

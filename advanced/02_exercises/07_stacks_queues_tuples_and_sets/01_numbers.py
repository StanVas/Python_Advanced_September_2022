first_set = set(map(int, input().split()))  # same as first = set([int(x) for x in input().split()])
second_set = set(map(int, input().split()))

number_of_commands = int(input())

for num in range(number_of_commands):
    command_parts = input().split()
    command = command_parts[0]
    target = command_parts[1]

    if command == 'Add':
        if target == 'First':
            first_set = first_set.union([int(x) for x in command_parts[2:]])
        else:
            second_set = second_set.union([int(x) for x in command_parts[2:]])
    elif command == 'Remove':
        if target == 'First':
            first_set = first_set.difference([int(x) for x in command_parts[2:]])
        else:
            second_set = second_set.difference([int(x) for x in command_parts[2:]])
    elif command == 'Check':
        # if first_set.issubset(second_set) or second_set.issubset(first_set):
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')

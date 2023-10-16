first_set = set()
second_set = set()

for num in range(1):
    command_parts = input().split()   # let's say: Add First 5 6 9 3
    command = command_parts[0]    # "Add"
    target = command_parts[1]     # "First"

    if command == 'Add':
        if target == 'First':           # we take the rest of the command_parts
            first_set = first_set.union([int(x) for x in command_parts[2:]]) # from index 2 to the end
        else:                 # make union   # in this case '5, 6, 9, 3'
            second_set = second_set.union([int(x) for x in command_parts[2:]])
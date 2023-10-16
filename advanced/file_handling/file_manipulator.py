import os

while True:
    command = input()
    if command == "End":
        break
    command = command.split('-')
    action = command[0]
    file_name = command[1]

    if action == 'Create':
        with open(file_name, "w") as file:
            pass

    elif action == 'Add':
        content = command[2]
        with open(file_name, "a") as file:
            file.write(f'{content}\n')

    elif action == 'Replace':
        old_str = command[2]
        new_str = command[3]
        try:
            with open(file_name, "r") as file:
                file_data = file.read()
                file_data = file_data.replace(old_str, new_str)
            with open(file_name, "w") as file:
                file.write(file_data)
        except FileNotFoundError:
            print('An error occurred')

    elif action == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

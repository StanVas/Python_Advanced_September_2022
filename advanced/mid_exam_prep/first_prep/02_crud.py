# https://judge.softuni.org/Contests/Practice/Index/3534#1
matrix = []

rows = 6
cols = 6

for _ in range(rows):
    matrix.append(list(input().split()))

position = input()
row = int(position[1])
col = int(position[4])

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(', ')
    action = command[0]
    direction = command[1]

    if direction == "up":
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    if action == "Create":
        value = command[2]
        if matrix[row][col] == '.':
            matrix[row][col] = value
        continue
    elif action == 'Update':
        value = command[2]
        if matrix[row][col] != '.':
            matrix[row][col] = value
        continue
    elif action == 'Read':
        if matrix[row][col] != '.':
            print(matrix[row][col])
        continue
    elif action == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'
        continue

for r in matrix:
    print(' '.join(r))

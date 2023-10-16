size = int(input())

matrix = []

for _ in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

while True:
    command = input()
    if command == 'END':
        break

    parts = command.split()
    action = parts[0]
    row, col, value = [int(x) for x in parts[1:]]

    if row < 0 or col < 0 or row >= size or col >= size:
        print('Invalid coordinates')
        continue

    if action == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, end='\n')

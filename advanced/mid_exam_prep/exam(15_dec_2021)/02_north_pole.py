rows, cols = list(map(int, input().split(', ')))

matrix = []
santa_row = 0
santa_col = 0
items = []
decorations = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}

for row in range(rows):
    matrix.append(input().split())

    for col in range(cols):
        if matrix[row][col] != '.':
            if matrix[row][col] == 'Y':
                santa_row = row
                santa_col = col
                matrix[santa_row][santa_col] = 'x'
            else:
                items.append(matrix[row][col])

command = input()
if command == 'End':
    matrix[santa_row][santa_col] = 'Y'

while command != 'End' and items:
    action = command.split('-')
    direction = action[0]
    steps = int(action[1])

    for step in range(steps):
        if direction == 'up':
            santa_row -= 1
        elif direction == 'down':
            santa_row += 1
        elif direction == 'left':
            santa_col -= 1
        elif direction == 'right':
            santa_col += 1

        if santa_row < 0:
            santa_row = rows - 1
        elif santa_row == rows:
            santa_row = 0
        if santa_col < 0:
            santa_col = cols - 1
        elif santa_col == cols:
            santa_col = 0

        if matrix[santa_row][santa_col] != 'x':
            if matrix[santa_row][santa_col] == 'D':
                decorations['Christmas decorations'] += 1
            elif matrix[santa_row][santa_col] == 'G':
                decorations['Gifts'] += 1
            elif matrix[santa_row][santa_col] == 'C':
                decorations['Cookies'] += 1
            if matrix[santa_row][santa_col] != '.':
                items.remove(matrix[santa_row][santa_col])
            matrix[santa_row][santa_col] = 'x'
            if not items:
                matrix[santa_row][santa_col] = 'Y'
                print('Merry Christmas!')
                break
        if not items:
            break
    if not items:
        break

    command = input()
    if command == 'End':
        matrix[santa_row][santa_col] = 'Y'

print("You've collected:")

for key, value in decorations.items():
    print(f'- {value} {key}')

for row in matrix:
    print(' '.join(row))

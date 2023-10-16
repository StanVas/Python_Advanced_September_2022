size = int(input())

matrix = []
alice_row = 0
alice_col = 0

for row in range(size):
    row_el = input().split()
    for col in range(size):
        if row_el[col] == 'A':
            alice_row = row
            alice_col = col
    matrix.append(row_el)

matrix[alice_row][alice_col] = '*'

collected_tea = 0
directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
    }

condition = False

while collected_tea < 10:
    if condition:
        break
    direction = input()
    row = 0
    col = 0
    if direction == 'right':
        row, col = directions[direction](alice_row, alice_col)
    elif direction == 'left':
        row, col = directions[direction](alice_row, alice_col)
    elif direction == 'up':
        row, col = directions[direction](alice_row, alice_col)
    elif direction == 'down':
        row, col = directions[direction](alice_row, alice_col)

    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col].isdigit():
            collected_tea += int(matrix[row][col])
            if collected_tea >= 10:
                matrix[row][col] = "*"
                break
        elif matrix[row][col] == 'R':
            condition = True
        matrix[row][col] = "*"
        alice_row = row
        alice_col = col
    else:    # if the coordinates are outside
        break

if collected_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
for row in matrix:
    print(' '.join(row))

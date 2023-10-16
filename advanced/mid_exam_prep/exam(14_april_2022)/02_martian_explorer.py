from collections import deque

SIZE = 6

field = []

rover_row = 0
rover_col = 0

deposits = {
    'Water': 0,
    'Metal': 0,
    'Concrete': 0,
}

for row in range(SIZE):
    field.append(input().split())
    if 'E' in field[row]:
        rover_row, rover_col = row, field[row].index('E')

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

command = deque(input().split(', '))

while command:
    current_direction = command.popleft()
    rover_row += directions[current_direction][0]
    rover_col += directions[current_direction][1]

    if rover_row == SIZE:
        rover_row = 0
    elif rover_row < 0:
        rover_row = 5
    elif rover_col == SIZE:
        rover_col = 0
    elif rover_col < 0:
        rover_col = 5

    if field[rover_row][rover_col] == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

    elif field[rover_row][rover_col] == 'W':
        deposits['Water'] += 1
        print(f'Water deposit found at ({rover_row}, {rover_col})')

    elif field[rover_row][rover_col] == 'M':
        deposits['Metal'] += 1
        print(f'Metal deposit found at ({rover_row}, {rover_col})')

    elif field[rover_row][rover_col] == 'C':
        deposits['Concrete'] += 1
        print(f'Concrete deposit found at ({rover_row}, {rover_col})')

if deposits['Water'] > 0 and deposits['Metal'] > 0 and deposits['Concrete'] > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')

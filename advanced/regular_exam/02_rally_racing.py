SIZE = int(input())

racing_number = int(input())

race_route = []

distance = 0

current_row = 0
current_col = 0
# finish_row = 0
# finish_col = 0

for row in range(SIZE):
    race_route.append(input().split())

    # for col in range(row):
    #     if race_route[row][col] == 'F':
    #         finish_row, finish_col = row, col

finished = False

while True:
    command = input()

    if command == 'End':
        break

    if command == 'up':
        current_row -= 1
    elif command == 'down':
        current_row += 1
    elif command == 'left':
        current_col -= 1
    elif command == 'right':
        current_col += 1

    if race_route[current_row][current_col] == "T":
        distance += 30
        race_route[current_row][current_col] = '.'
        for row in range(SIZE):
            for col in range(SIZE):
                if race_route[row][col] == 'T':
                    current_row = row
                    current_col = col
                    race_route[current_row][current_col] = '.'

    elif race_route[current_row][current_col] == "F":
        distance += 10
        finished = True
        break

    else:
        distance += 10


if finished:
    print(f'Racing car {racing_number} finished the stage!')
else:
    print(f'Racing car {racing_number} DNF.')

print(f'Distance covered {distance} km.')

race_route[current_row][current_col] = 'C'

for row in race_route:
    print(''.join(row))

SIZE = 7

players = input().split(', ')
key_dict = {key for key in players}  # only making the keys
players_dict = dict.fromkeys(key_dict, 501)  # giving default value for every key: 501
player_one_hits = 0

matrix = []

for row in range(SIZE):
    matrix.append(input().split())


win_condition = False
throws = 0

while not win_condition:
    throws += 1
    coordinates = input().strip('()').split(', ')
    row = int(coordinates[0])
    col = int(coordinates[1])
    current_player = players[0]

    win_throw = throws / 2
    if win_throw < 1:
        win_throw = 1
    elif not win_throw.is_integer():
        win_throw += 1

    if 0 > row or row >= SIZE:
        players[0], players[1] = players[1], players[0]
        continue
    elif 0 > col or col >= SIZE:
        players[0], players[1] = players[1], players[0]
        continue

    if matrix[row][col] == 'B':
        win_condition = True
        print(f'{current_player} won the game with {int(win_throw)} throws!')
        break

    elif matrix[row][col] != 'D' and matrix[row][col] != 'T':
        players_dict[current_player] -= int(matrix[row][col])

    elif matrix[row][col] == 'D':
        hit = ((int(matrix[row][0]) + int(matrix[row][6])) + (int(matrix[0][col]) + int(matrix[6][col]))) * 2
        players_dict[current_player] -= hit

    elif matrix[row][col] == 'T':
        hit = ((int(matrix[row][0]) + int(matrix[row][6])) + (int(matrix[0][col]) + int(matrix[6][col]))) * 3
        players_dict[current_player] -= hit

    if players_dict[current_player] <= 0:
        win_condition = True
        print(f'{current_player} won the game with {int(win_throw)} throws!')
        break

    players[0], players[1] = players[1], players[0]

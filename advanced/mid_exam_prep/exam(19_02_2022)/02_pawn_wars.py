SIZE = 8
chess_board = []

white_row = 0
white_col = 0
black_row = 0
black_col = 0

position_row = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1',
}

position_col = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}

for row in range(SIZE):
    row_data = input().split()
    for col in range(SIZE):
        if row_data[col] == 'w':
            white_row = row
            white_col = col
        elif row_data[col] == 'b':
            black_row = row
            black_col = col
    chess_board.append(row_data)

turn = ['w', 'b']

for _ in range(22):
    player = turn[0]

    if player == 'w':
        if black_row == white_row - 1 and (black_col == white_col - 1 or black_col == white_col + 1):
            white_row = position_row[black_row]
            white_col = position_col[black_col]
            print(f'Game over! White win, capture on {white_col}{white_row}.')
            break
        else:
            white_row -= 1
            if white_row == 0:
                white_row = position_row[white_row]
                white_col = position_col[white_col]
                print(f"Game over! White pawn is promoted to a queen at {white_col}{white_row}.")
                break

    elif player == 'b':
        if white_row == black_row + 1 and (white_col == black_col - 1 or white_col == black_col + 1):
            black_row = position_row[white_row]
            black_col = position_col[white_col]
            print(f'Game over! Black win, capture on {black_col}{black_row}.')
            break
        else:
            black_row += 1
            if black_row == 7:
                black_row = position_row[black_row]
                black_col = position_col[black_col]
                print(f"Game over! Black pawn is promoted to a queen at {black_col}{black_row}.")
                break

    turn[0], turn[1] = turn[1], turn[0]
    continue

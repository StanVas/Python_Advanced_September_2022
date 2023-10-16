def damage_coordinates(mat, r, c):
    possible_damage_coordinates = [
        [r - 1, c - 1],
        [r - 1, c],
        [r - 1, c + 1],
        [r, c - 1],
        [r, c + 1],
        [r + 1, c - 1],
        [r + 1, c],
        [r + 1, c + 1],
    ]
    result = []
    for dmg_row, dmg_col in possible_damage_coordinates:
        if 0 <= dmg_row < len(mat) and 0 <= dmg_col < len(mat) and mat[dmg_row][dmg_col] > 0:
            result.append([dmg_row, dmg_col])
    return result


size = int(input())

matrix = []

for row in range(size):
    matrix.append(list(map(int, input().split())))  # one way

bomb_coordinates = input().split()

for bomb in bomb_coordinates:
    row, col = [int(x) for x in bomb.split(',')]  # second way(doing the same)
    power = matrix[row][col]

    if power <= 0:
        continue

    matrix[row][col] = 0

    damage = damage_coordinates(matrix, row, col)
    for row, col in damage:
        matrix[row][col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells_count}')
print(f'Sum: {alive_cells_sum}')
for row in matrix:
    print(*row, sep=' ')

rows, columns = list(map(int, input().split()))

string = input()
snake_str = []
for let in string:
    snake_str.append(let)

matrix = []

for row in range(rows):
    current_str = []
    for col in range(columns):
        current_str.append(snake_str[0])
        snake_str.append(snake_str.pop(0))
    if row % 2 != 0:
        current_str = current_str[::-1]
    matrix.append(current_str)

for row in matrix:
    print(''.join(row))

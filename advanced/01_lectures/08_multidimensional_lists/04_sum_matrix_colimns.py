rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    # row = [int(x) for x in input().split()]
    # matrix.append(row)
    # one line =
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    result = 0
    for row in range(rows):
        result += matrix[row][col]
    print(result)

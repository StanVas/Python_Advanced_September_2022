rows, columns = list(map(int, input().split()))

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

result = 0

for row in range(rows - 1):
    for col in range(columns -1):
        ch = matrix[row][col]
        if ch == matrix[row][col + 1] and ch == matrix[row + 1][col] and ch == matrix[row + 1][col + 1]:
            result += 1

print(result)

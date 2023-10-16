rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

diagonal_result = 0

for idx in range(rows):
    diagonal_result += matrix[idx][idx]

print(diagonal_result)

size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])
primary_diagonal = 0
secondary_diagonal = 0
for idx in range(size):
    primary_diagonal += matrix[idx][idx]
    secondary_diagonal += matrix[idx][size - 1 - idx]

print(abs(primary_diagonal - secondary_diagonal))

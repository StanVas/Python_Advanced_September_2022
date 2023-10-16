### finding col and row with enumerate
matrix_4 = [
    [1, 2, 3, 4],
    [4, 5, 6],
    [7, 8]
]
for idx, row in enumerate(matrix_4):
    print(idx, row)

### directly adding list(input()) into matrix
size = int(input())
matrix = []
for _ in range(size):
    matrix.append(list(input()))
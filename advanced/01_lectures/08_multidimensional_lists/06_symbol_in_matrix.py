size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

target_chr = input()
condition = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == target_chr:
            condition = True
            print(f'({row}, {col})')
            break
    if condition:
        break

if not condition:
    print(f'{target_chr} does not occur in the matrix')

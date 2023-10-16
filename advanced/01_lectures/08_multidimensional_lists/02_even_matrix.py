rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(row)
    # second way
    # row = [int(x) for x in input().split(', ')
    # matrix.append([x for x in row if x % 2 == 0])
print(matrix)

rows, columns = list(map(int, input().split()))
starting_chr = 97
matrix = []

for row in range(rows):
    first_ch = starting_chr + row
    second_ch = starting_chr + row
    third_ch = starting_chr + row
    sub = []
    for col in range(columns):
        sub.append(chr(first_ch) + chr(second_ch) + chr(third_ch))
        second_ch += 1

    matrix.append(sub)

for row in matrix:
    print(' '.join(row))

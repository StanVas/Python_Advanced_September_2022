def print_line(n):
    # 1 2 3 4
    # 1 2 3
    # 1 2
    # 1
    # print(*[num for num in range(1, n + 1)], sep=' ')
    print(*[num for num in range(1, n + 1)], sep='<->')


def print_triangle(n):
    pass
    # for row in range(1, size + 1):
    #     for col in range(1, row + 1):
    #         print(col, end=' ')
    #     print()
    # for row in range(size - 1, 0, -1):
    #     for col in range(1, row + 1):
    #         print(col, end=' ')
    #     print()
    for row in range(1, n + 1):
        print_line(row)

    for row in range(n -1, 0, -1):
        print_line(row)


def print_square(n):
    for _ in range(1, n + 1):
        print_line(n)


def print_rectangle(rows, cols):
    for _ in range(1, rows + 1):
        print_line(cols)

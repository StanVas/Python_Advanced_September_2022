def even_odd(*args):

    def even():
        result = []
        for idx in range(len(args) - 1):
            if args[idx] % 2 == 0:
                result.append(args[idx])
        return result

    def odd():
        result = []
        for idx in range(len(args) - 1):
            if args[idx] % 2 != 0:
                result.append(args[idx])
        return result

    operator = args[-1]

    if operator == 'even':
        return even()
    elif operator == 'odd':
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

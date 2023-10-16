def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(2, 5))  # in this case
# 2 ^ 5
# 2 * 2 ^ 4
# 2 * 2 ^ 3
# 2 * 2 ^ 2
# 2 * 2 ^ 1
# 2 ^ 0 == 1  base case


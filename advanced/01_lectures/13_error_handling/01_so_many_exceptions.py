numbers_list = list(map(int, input().split(", ")))
result = 1

for num in numbers_list:
    if num <= 5:
        result *= num
    elif num <= 10:
        result /= num

print(result)


# input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# multiply until 5
# divide from 5 to 10

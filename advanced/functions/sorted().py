dictionary = {
    'ivan': 14,
    'mimi': 14,
    'gosho': 19,
    'ani': 14
}

# 1. Age in ascending order
# 2. Name length in descending order
# 3. Name in ascending order

result = sorted(dictionary.items(), key=lambda x: (x[1], len(x[0]), x[0]))
print(result)


# 4. Reverse
                                                      # (age)
second_result = sorted(dictionary.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
third_result = sorted(dictionary.items(), key=lambda x: (x[1], len(x[0]), x[0]), reverse=True)
print(second_result)
print(third_result)

# sorted() returns tuple
dictionary = {'odd': [1, 2, 3], 'even': [3, 4, 5, 7, 10, 2, 5, 5, 2]}

print(sorted(dictionary.items(), key=lambda x: len(x)))
         # in this case sorted returns tupple with 2 elements key: value

# if we want to make it dict again we can say:
print(dict(sorted(dictionary.items(), key=lambda x: -len(x[1]))))

# while in key=lambda x: -len(x[1]) -> x[1] is the value and x or x[0] the key
some_dict = {
    'flowers': ('rose', 'dahlia', 'water lilly'),
    'cars': ('wv', 'bmw', 'audi', 'nissan'),
    'numbers': ('one', 'two')
}
                                              # descending        # then x[0] gives
                                            # cars and flowers    # key in ascending order
                                        # have 4 items as values  # so 'c' is before 'f'
some_dict = sorted(some_dict.items(), key=lambda x: (-len(x[1]), x[0]))

print(some_dict)

# gives back dictionary
some_dict2 = {
    'flowers': ('rose', 'dahlia', 'water lilly'),
    'cars': ('wv', 'bmw', 'audi', 'nissan'),
    'numbers': ('one', 'two')
}

some_dict2 = dict(sorted(some_dict2.items(), key=lambda x: (-len(x[1]))))
print(some_dict2)

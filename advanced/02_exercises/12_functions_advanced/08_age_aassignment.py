def age_assignment(*args, **kwargs):
    names_dict = {}

    for el in args:
        first_let = el[0]
        name = el
        for key, value in kwargs.items():
            if first_let == key:
                names_dict[name] = value
    sorted_names = dict(sorted(names_dict.items(), key=lambda x: (x[0])))
    sorted_result = [f'{key} is {value} years old.' for key, value in sorted_names.items()]
    return '\n'.join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# second way with less code in the function
# def age_assignment(*args, **kwargs):
#     result = {}
#     for name in args:
#         first_let = name[0]   # we take the first letter from args
#         age = kwargs[first_let]   # directly get the age from the dictionary
#         result[name] = age
#
#     sorted_result = [f'{key} is {value} years old.' for key, value in sorted(result.items(), key=lambda x: x[0])]
#     return '\n'.join(sorted_result)
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

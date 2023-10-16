numbers_dictionary = {}

while True:
    line = input()
    if line == 'Search':
        break

    try:
        number_as_string = line
        number_as_value = int(input())
        numbers_dictionary[number_as_string] = number_as_value
    except ValueError:
        print('The variable number must be an integer')

while True:
    if line == 'Remove':
        break
    if line == 'Search':
        number_for_search = input()
        if number_for_search == 'Remove':
            break
        try:
            print(numbers_dictionary[number_for_search])
        except KeyError:
            print("Number does not exist in dictionary")
    line = input()

while True:
    if line == 'End':
        break
    if line == 'Remove':
        number_to_remove = input()
        if number_to_remove == 'End':
            break
        try:
            del numbers_dictionary[number_to_remove]
        except KeyError:
            print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)

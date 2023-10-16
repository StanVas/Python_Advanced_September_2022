def words_sorting(*words):
    words_values = {}
    total_sum = 0

    for word in words:
        words_values[word] = 0
        for letter in word:
            words_values[word] += ord(letter)
            total_sum += ord(letter)

    result = []

    if total_sum % 2 == 0:
        even_result = sorted(words_values.items(), key=lambda x: x[0])
        for key, value in even_result:
            result.append(f'{key} - {value}')
        return '\n'.join(result)

    else:
        odd_result = sorted(words_values.items(), key=lambda x: -x[1])
        for key, value in odd_result:
            result.append(f'{key} - {value}')
        return '\n'.join(result)


print(
    words_sorting('escape', 'charm', 'mythology'))

print(
    words_sorting('escape', 'charm', 'eye'))

print(words_sorting('cacophony', 'accolade'))

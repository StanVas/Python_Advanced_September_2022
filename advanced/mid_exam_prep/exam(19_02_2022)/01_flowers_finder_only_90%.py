from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers = {
    'rose': ['r', 'o', 's', 'e'],
    'tulip': ['t', 'u', 'l', 'i', 'p'],
    'lotus': ['l', 'o', 't', 'u', 's'],
    'daffodil': ['d', 'a', 'f', 'o', 'i', 'l']
}

condition = False

while True:
    for key, value in flowers.items():
        if len(value) == 0:
            print(f'Word found: {key}')
            condition = True
    if condition:
        break

    if not vowels:
        print('Cannot find any word!')
        break
    else:
        current_vowel = vowels.popleft()

    if not consonants:
        print('Cannot find any word!')
        break
    else:
        current_consonant = consonants.pop()

    for values in flowers.values():
        if current_vowel in values:
            values.remove(current_vowel)
            if len(values) == 0:
                break
        if current_consonant in values:
            values.remove(current_consonant)
            if len(values) == 0:
                break

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')

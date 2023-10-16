text = input()
char_dict = {}

for ch in text:
    if ch not in char_dict:
        char_dict[ch] = 1
    else:
        char_dict[ch] += 1

sorted_dict = sorted(char_dict.items())

for key, value in sorted_dict:
    print(f'{key}: {value} time/s')

string = list(input())
reversed_string = []

while string:
    new = string.pop()
    reversed_string.append(new)

print(''.join(reversed_string))

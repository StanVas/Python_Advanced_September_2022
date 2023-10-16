email = input().split('@')

print(email)




import re


def valid_email(some_email):
    pattern = r'(\w{4,})(@)'
    result = re.findall(pattern, some_email)
    if not result:
        return print("Name must be more than 4 characters")
    return email





while True:
    command = input()

    if command == 'End':
        break

    email = command
    length = too_short(email)
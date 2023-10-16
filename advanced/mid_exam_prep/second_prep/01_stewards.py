# https://judge.softuni.org/Contests/Practice/Index/3534#0

from collections import deque

seats = input().split(', ')

first_seq = deque(map(int, input().split(', ')))
second_seq = deque(map(int, input().split(', ')))

# taken_seats = []
rotations = 0
seat_matches = []

while True:
    if len(seat_matches) == 3 or rotations == 10:
        break

    rotations += 1

    first_num = first_seq.popleft()
    second_num = second_seq.pop()

    letter = chr(first_num + second_num)
    first_seat = str(first_num) + letter
    second_seat = str(second_num) + letter

    if first_seat in seat_matches or second_seat in seat_matches:
        continue

    if first_seat in seats:
        seat_matches.append(first_seat)
        continue
    elif second_seat in seats:
        seat_matches.append(second_seat)
        continue
    else:
        first_seq.append(first_num)
        second_seq.appendleft(second_num)

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotations}')

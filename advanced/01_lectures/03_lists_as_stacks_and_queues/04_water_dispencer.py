from collections import deque

available_water = int(input())
water_queue = deque()

while True:
    line = input()
    if line == 'Start':
        break
    water_queue.append(line)

while True:
    line = input()
    if line == 'End':
        print(f'{available_water} liters left')
        break
    line_args = line.split()

    if len(line_args) == 2:   # refill command
        available_water += int(line_args[1])

    else:
        water_needed = int(line)
        person = water_queue.popleft()
        if water_needed > available_water:
            print(f'{person} must wait')
        else:
            available_water -= water_needed
            print(f'{person} got water')

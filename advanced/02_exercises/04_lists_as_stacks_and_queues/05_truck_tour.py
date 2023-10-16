from collections import deque

number_of_pumps = int(input())
petrol_pumps = deque()

for pump in range(number_of_pumps):
    petrol_pumps.append(input().split())

starting_pump = 0
fuel = 0
condition = False

for test in range(number_of_pumps):
    petrol_pumps_copy = petrol_pumps.copy()
    if condition:
        break
    for pump in range(number_of_pumps):
        current_pump = petrol_pumps_copy.popleft()
        current_fuel = int(current_pump[0])
        current_distance = int(current_pump[1])
        fuel += current_fuel
        if fuel < current_distance:
            starting_pump += 1
            fuel = 0
            swap = petrol_pumps.popleft()
            petrol_pumps.append(swap)
            break
        else:
            fuel -= current_distance
            petrol_pumps_copy.append(current_pump)
            if pump == number_of_pumps:
                condition = True

print(starting_pump)

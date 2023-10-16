from collections import deque

caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

total_caffeine = 0

while caffeine and energy_drinks:
    mg_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()
    current_caffeine = mg_caffeine * current_drink

    if total_caffeine + current_caffeine <= 300:
        total_caffeine += current_caffeine

    else:
        energy_drinks.append(current_drink)
        if total_caffeine - 30 >= 0:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')

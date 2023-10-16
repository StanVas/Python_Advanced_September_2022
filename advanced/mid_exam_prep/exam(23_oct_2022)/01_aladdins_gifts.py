from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

wedding_presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    total_sum = current_material + current_magic
    if total_sum < 100:
        if total_sum % 2 == 0:
            total_sum = current_material * 2 + current_magic * 3
        else:
            total_sum *= 2
    elif total_sum > 499:
        total_sum /= 2

    if 100 <= total_sum <= 199:
        wedding_presents['Gemstone'] += 1
    elif 200 <= total_sum <= 299:
        wedding_presents['Porcelain Sculpture'] += 1
    elif 300 <= total_sum <= 399:
        wedding_presents['Gold'] += 1
    elif 400 <= total_sum <= 499:
        wedding_presents['Diamond Jewellery'] += 1

if wedding_presents['Gemstone'] > 0 and wedding_presents['Porcelain Sculpture'] > 0:
    print("The wedding presents are made!")
elif wedding_presents['Gold'] > 0 and wedding_presents['Diamond Jewellery'] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    result = list(map(str, materials))
    print(f'Materials left: {", ".join(result)}')
if magic_level:
    result = list(map(str, magic_level))
    print(f'Magic left: {", ".join(result)}')

sorted_gifts = [f"{key}: {value}" for key, value in sorted(wedding_presents.items(), key=lambda x: x[0]) if value > 0]
print('\n'.join(sorted_gifts))

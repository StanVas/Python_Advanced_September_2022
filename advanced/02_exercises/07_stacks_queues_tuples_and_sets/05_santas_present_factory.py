from collections import deque

material_values = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

toys = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

total_toys = {}

while material_values and magic_levels:
    material = material_values.pop()
    magic = magic_levels.popleft()

    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_levels.appendleft(magic)
        continue
    if magic == 0:
        material_values.append(material)
        continue

    result = material * magic
    if result in toys.keys():
        toy = toys[result]
        if toy not in total_toys:
            total_toys[toy] = 0
        total_toys[toy] += 1
        continue

    if result < 0:
        material_values.append(material + magic)
    elif result not in toys and result > 0:
        material_values.append(material + 15)

condition = False
if 'Doll' in total_toys and 'Wooden train' in total_toys:
    condition = True
elif 'Teddy bear' in total_toys and 'Bicycle' in total_toys:
    condition = True

if condition:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_values:
    print(f"Materials left: {', '.join(str(x) for x in reversed(material_values))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key in sorted(total_toys):
    value = total_toys[key]
    print(f'{key}: {value}')

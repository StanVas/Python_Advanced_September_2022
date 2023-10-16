from collections import deque

elfs_energy = deque(map(int, input().split()))
materials = list(map(int, input().split()))

energy_spent = 0
toys_made = 0
counter = 0

while elfs_energy and materials:
    current_elf_en = elfs_energy.popleft()

    if current_elf_en < 5:
        continue

    counter += 1

    current_material = materials.pop()

    if counter % 3 != 0:
        if current_elf_en >= current_material:
            if counter % 5 == 0:
                current_elf_en -= current_material
            else:
                current_elf_en -= current_material - 1
                toys_made += 1
            elfs_energy.append(current_elf_en)
            energy_spent += current_material
        else:
            current_elf_en *= 2
            elfs_energy.append(current_elf_en)
            materials.append(current_material)

    if counter % 3 == 0:
        if current_elf_en >= current_material * 2:
            if counter % 5 == 0:
                current_elf_en -= current_material * 2
            else:
                current_elf_en -= (current_material * 2) - 1
                toys_made += 2
            energy_spent += current_material * 2
            elfs_energy.append(current_elf_en)
        else:
            current_elf_en *= 2
            elfs_energy.append(current_elf_en)
            materials.append(current_material)

print(f'Toys: {toys_made}')
print(f'Energy: {energy_spent}')
if elfs_energy:
    print(f'Elves left: {", ".join(str(x) for x in elfs_energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')

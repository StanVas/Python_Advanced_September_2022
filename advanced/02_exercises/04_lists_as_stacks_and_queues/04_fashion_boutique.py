box_of_clothes = list(map(int, input().split()))

rack_capacity = int(input())
current_rack_cap = rack_capacity
number_of_racks = 1

while box_of_clothes:
    current_cloth = box_of_clothes.pop()
    if current_cloth > current_rack_cap:
        number_of_racks += 1
        current_rack_cap = rack_capacity
        current_rack_cap -= current_cloth
    else:
        current_rack_cap -= current_cloth

print(number_of_racks)

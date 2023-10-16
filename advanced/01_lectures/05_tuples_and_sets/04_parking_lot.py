lines = int(input())
num_plates_set = set()

for line in range(lines):
    action, number_plate = input().split(', ')
    if action == 'IN':
        num_plates_set.add(number_plate)
    else:
        num_plates_set.remove(number_plate)

if num_plates_set:
    print("\n".join(num_plates_set))
else:
    print('Parking Lot is Empty')

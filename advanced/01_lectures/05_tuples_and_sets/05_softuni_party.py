number_of_guests = int(input())
vip = set()
regular = set()

for num in range(number_of_guests):
    guest_code = input()
    if guest_code[0].isdigit():
        vip.add(guest_code)
    else:
        regular.add(guest_code)

while True:
    code = input()
    if code == 'END':
        break
    else:
        if code in vip:
            vip.remove(code)
        elif code in regular:
            regular.remove(code)

did_not_come = 0
if vip:
    did_not_come += len(vip)
if regular:
    did_not_come += len(regular)
print(did_not_come)
sorted_vip = sorted(vip)
sorted_reg = sorted(regular)
if vip:
    print("\n".join(sorted_vip))
if regular:
    print("\n".join(sorted_reg))

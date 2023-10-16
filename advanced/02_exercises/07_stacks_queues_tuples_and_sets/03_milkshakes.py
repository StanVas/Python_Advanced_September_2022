from collections import deque

chocolate_stack = [int(x) for x in input().split(', ')]
milk_cups_queue = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolate_stack and milk_cups_queue and milkshakes < 5:
    chocolate = chocolate_stack.pop()
    milk = milk_cups_queue.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups_queue.appendleft(milk)
        continue
    if milk <= 0:
        chocolate_stack.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups_queue.append(milk)
        chocolate_stack.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_stack:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_stack])}")
else:
    print('Chocolate: empty')

if milk_cups_queue:
    print(f"Milk: {', '.join([str(x) for x in milk_cups_queue])}")
else:
    print("Milk: empty")

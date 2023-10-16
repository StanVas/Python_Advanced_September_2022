from collections import deque

ramen = list(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while ramen and customers:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()

    if current_ramen == current_customer:
        continue

    elif current_ramen > current_customer:
        current_ramen -= current_customer
        ramen.append(current_ramen)

    elif current_ramen < current_customer:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if not customers:
    print('Great job! You served all the customers.')
    if ramen:
        ramen = list(map(str, ramen))
        print(f"Bowls of ramen left: {', '.join(ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    customers = list(map(str, customers))
    print(f"Customers left: {', '.join(customers)}")

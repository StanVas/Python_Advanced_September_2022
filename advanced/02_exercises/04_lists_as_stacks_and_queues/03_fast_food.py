from collections import deque

total_food = int(input())

daily_orders = deque(map(int, input().split()))

print(max(daily_orders))

while daily_orders:
    if daily_orders[0] > total_food:
        orders_to_print = []
        while daily_orders:
            order = str(daily_orders.popleft())
            orders_to_print.append(order)
        print(f'Orders left: {" ".join(orders_to_print)}')
        break
    else:
        order = daily_orders.popleft()
        total_food -= order
    if not daily_orders:
        print(f'Orders complete')

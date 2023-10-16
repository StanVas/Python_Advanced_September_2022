from collections import deque

orders = deque(int(x) for x in input().split(', '))
employees = list(int(x) for x in input().split(', '))
pizzas_made = 0

while orders and employees:
    current_order = orders.popleft()

    if current_order > 10 or current_order <= 0:
        continue

    current_employee = employees.pop()

    if current_employee >= current_order:
        pizzas_made += current_order

    elif current_employee < current_order:
        current_order -= current_employee
        pizzas_made += current_employee
        orders.appendleft(current_order)

if orders:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in orders)}')
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    if employees:
        print(f'Employees: {", ".join(str(x) for x in employees)}')

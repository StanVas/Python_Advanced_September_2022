from collections import deque
working_bees = deque(map(int, input().split()))
nectar_value = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while working_bees and nectar_value:
    bee = working_bees.popleft()
    nectar = nectar_value.pop()

    if nectar < bee:
        working_bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = symbols.popleft()
    total_honey += abs(operations[operator](bee, nectar))

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")

if nectar_value:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_value])}")

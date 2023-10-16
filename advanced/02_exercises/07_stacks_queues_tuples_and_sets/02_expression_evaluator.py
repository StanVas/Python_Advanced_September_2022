from collections import deque

expression = input().split()
numbers_queue = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for ch in expression:
    if ch in '+-/*':
        while len(numbers_queue) > 1:
            left_num = numbers_queue.popleft()
            right_num = numbers_queue.popleft()
            result = operations[ch](left_num, right_num)
            numbers_queue.appendleft(result)
    else:
        numbers_queue.append(int(ch))

print(numbers_queue.popleft())

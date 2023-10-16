from collections import deque

expression = input().split()
numbers_queue = deque()

operations = {
    '+': lambda a, b: a + b,   # use lambda for operation
    '-': lambda a, b: a - b,   # key: contains operation with two values
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for ch in expression:
    if ch in '+-/*':
        while len(numbers_queue) > 1:
            left_num = numbers_queue.popleft()
            right_num = numbers_queue.popleft()
            result = operations[ch](left_num, right_num)
    # we use the key(in first case '-') and give two values(in first case - 6 and 3)
            numbers_queue.appendleft(result)
    else:
        numbers_queue.append(int(ch))

print(numbers_queue.popleft())

# input = 6 3 - 2 1 * 5 /
from collections import deque

kids_queue = deque(input().split())
n = int(input())
counter = 1

while len(kids_queue) > 1:
    kid = kids_queue.popleft()

    if counter == n:
        print(f'Removed {kid}')
        counter = 1

    else:
        counter += 1
        kids_queue.append(kid)

last_kid = kids_queue.popleft()
print(f'Last is {last_kid}')

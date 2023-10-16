from collections import deque
from datetime import datetime

robots = input().split(';')

robots_dict = {}

for item in robots:
    item = item.split('-')
    name = item[0]
    time = int(item[1])
    robots_dict[name] = time

robots_queue = deque(name for name in robots_dict.keys())
product_queue = deque()
hour, min, sec = input().split(':')
if sec > 59:
    min += 1
    sec = abs(sec - 60)
if min > 59:
    hour += 1
    min = abs(sec - 60)

while True:
    product = input()
    if product == 'End':
        break
    else:
        current_robot = robots_queue.popleft()
        if hour == hour and min == min and sec == sec:
            sec += 1
        print(f'{current_robot} - {product} [{hour}:{min}:{sec}]')
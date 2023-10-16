from collections import deque
# https://judge.softuni.org/Contests/Practice/Index/3515#0

eggs = deque(map(int, input().split(', ')))
papers = list(map(int, input().split(', ')))
boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    elif egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    paper = papers.pop()
    if egg + paper <= 50:
        boxes += 1
        continue

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    # print(f'Eggs left: {", ".join(list(map(str, eggs)))}')
    print(f'Eggs left: ', end="")
    print(*eggs, sep=', ')
if papers:
    print(f'Pieces of paper left: {", ".join(list(map(str, papers)))}')

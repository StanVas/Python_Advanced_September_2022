from collections import deque

colors = deque(input().split())
colors_collection = []
primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

while colors:
    left = colors.popleft()
    right = colors.pop() if colors else ''

    result = left + right
    if result in primary_colors or result in secondary_colors:
        colors_collection.append(result)
        continue
    result = right + left
    if result in primary_colors or result in secondary_colors:
        colors_collection.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        colors.insert(len(colors) // 2, left)
    if right:
        colors.insert(len(colors) // 2, right)

forming_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

result = []

for color in colors_collection:
    if color in primary_colors:
        result.append(color)
        continue

    is_collected = True
    for primary in forming_colors[color]:
        if primary not in colors_collection:
            is_collected = False
            break
    if is_collected:
        result.append(color)

print(result)

number_of_lines = int(input())
set_of_elements = set()

for num in range(number_of_lines):
    element = input().split()
    for item in element:
        set_of_elements.add(item)

for item in set_of_elements:
    print(item)

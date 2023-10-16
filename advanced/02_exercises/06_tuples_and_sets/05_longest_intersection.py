import re
number_of_intersections = int(input())
pattern = r'\d+'
lst_of_intersections = []
for _ in range(number_of_intersections):
    current_intersection = input()
    pattern = r'\d+'
    matches = re.findall(pattern, current_intersection)
    first_num, second_num, third_num, forth_num = [int(el) for el in matches]
    first_seq = range(first_num, second_num + 1)
    second_seq = range(third_num, forth_num + 1)
    intersection = set(first_seq).intersection(set(second_seq))
    lst_of_intersections.append(intersection)

longest = sorted(lst_of_intersections, key=lambda x: -(len(x)))[0]
print(f'Longest intersection is {list(longest)} with length {len(longest)}')

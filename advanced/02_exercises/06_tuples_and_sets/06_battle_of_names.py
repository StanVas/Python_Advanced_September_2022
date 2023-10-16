number_of_names = int(input())
odd_set = set()
even_set = set()

for num in range(1, number_of_names + 1):
    name = input()
    name_value = 0
    for ch in name:
        name_value += ord(ch)
    total_value = name_value // num
    if total_value % 2 == 0:
        even_set.add(total_value)
    else:
        odd_set.add(total_value)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    modified_set = [str(el) for el in odd_set.union(even_set)]
    print(f", ".join(modified_set))
elif odd_sum > even_sum:
    modified_set = [str(el) for el in odd_set.difference(even_set)]
    print(f", ".join(modified_set))
elif odd_sum < even_sum:
    modified_set = [str(el) for el in odd_set.symmetric_difference(even_set)]
    print(f", ".join(modified_set))

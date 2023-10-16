number_of_names = int(input())
set_of_names = set()

for num in range(number_of_names):
    name = input()
    set_of_names.add(name)

print("\n".join(set_of_names))

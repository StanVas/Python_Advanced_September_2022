input_str = input().split('|')

result = []

for idx in range(len(input_str) - 1, -1, -1):
    current_elements = input_str[idx].strip().split()
    result.extend(current_elements)

print(' '.join(result))

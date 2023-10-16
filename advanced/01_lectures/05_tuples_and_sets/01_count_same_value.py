numbers = list(map(float, input().split()))
checked_nums = []
for num in numbers:
    if num in checked_nums:
        continue
    else:
        count = numbers.count(num)
        checked_nums.append(num)
        print(f'{num} - {count} times')

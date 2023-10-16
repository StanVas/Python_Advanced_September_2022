def parse_line(line):
    args = line.split()
    return ('Create', int(args[2])) if args[0] == 'Create' else ('Locate', int(args[1]))


def create(num):
    result = [0, 1]
    for _ in range(num - 2):
        num1 = result[-1]
        num2 = result[-2]
        result.append(num1 + num2)
    return result


def locate(target, nums):
    for idx in range(len(nums)):
        current_num = nums[idx]
        if current_num == target:
            return idx
    return -1

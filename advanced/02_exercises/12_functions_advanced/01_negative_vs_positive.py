def negative_vs_positive(*args):
    positive_sum = 0
    negative_sum = 0
    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num

    return positive_sum, negative_sum


numbers = [int(x) for x in input().split()]

positive_sum, negative_sum = negative_vs_positive(*numbers)

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print('The negatives are stronger than the positives')
else:
    print("The positives are stronger than the negatives")

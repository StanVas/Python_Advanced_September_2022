numbers = [{1, 2}, {3, 4, 5}, {6, 7, 8, 9, 10}]

                      # here reverse the sort and takes from index 0(a.k. the first one)
                      # in this case the longest one(when we reverse it)
longest = sorted(numbers, key=lambda x: -(len(x)))[0]
print(f'Longest list is {list(longest)} with length {len(longest)}')
                    # here converts to list
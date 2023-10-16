# creating a matrix with zeros
matrix = [[0 for j in range(2)] for i in range(3)]
print(matrix)

# creating a matrix with numbers
matrix_2 = [[j for j in range(1, 4)] for i in range(3)]
print(matrix_2)


# flattening a matrix
matrix_3 = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix_3 for num in sublist]
print(flattened)
# with for loop
result = []
for row in matrix_3:
    result.extend(row)
print(result)
####
result_2 = []
[result_2.extend(row) for row in matrix_3]
print(result_2)




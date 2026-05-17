# 4 a. Create a matrix and perform the following: Add and subtract two matrices. 
# Find the transpose of a matrix. Write a program to perform matrix multiplication. 

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

addition = [[0, 0], [0, 0]]
subtraction = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        addition[i][j] = A[i][j] + B[i][j]
        subtraction[i][j] = A[i][j] - B[i][j]

print("Addition:")
for row in addition:
    print(row)

print("Subtraction:")
for row in subtraction:
    print(row)






matrix = [[1, 2, 3],[4, 5, 6]]

transpose = []

for i in range(len(matrix[0])):
    row = []

    for j in range(len(matrix)):
        row.append(matrix[j][i])

    transpose.append(row)

print("Transpose Matrix:")
for row in transpose:
    print(row)







A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0, 0],
          [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix Multiplication Result:")

for row in result:
    print(row)


# b. Write a program to generate a multiplication table for numbers from 1 to 10.


for i in range(1, 11):
    print("\nTable of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
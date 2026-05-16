# f. Create a matrix and perform the following:
# Add and subtract two matrices. 
# Find the transpose of a matrix. 
# Write a program to perform matrix multiplication.
# Implement a program to check if a given matrix is symmetric.



# Matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Addition
print("Addition:")
for i in range(2):
    row = []
    for j in range(2):
        row.append(A[i][j] + B[i][j])
    print(row)

# Subtraction
print("\nSubtraction:")
for i in range(2):
    row = []
    for j in range(2):
        row.append(A[i][j] - B[i][j])
    print(row)

# Transpose
print("\nTranspose:")
for i in range(2):
    row = []
    for j in range(2):
        row.append(A[j][i])
    print(row)

# Matrix Multiplication
print("\nMultiplication:")
result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)

# Symmetric Matrix Check
symmetric = True

for i in range(2):
    for j in range(2):
        if A[i][j] != A[j][i]:
            symmetric = False

if symmetric:
    print("\nMatrix is Symmetric")
else:
    print("\nMatrix is Not Symmetric")
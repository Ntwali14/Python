matrix1=[]
matrix2=[]
matrix3=[]

m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of columns: "))

# Input first matrix
print("Enter the elements  matrix1: ")
for i in range(m):
    row=[]
    for j in range(n):
        ele = int(input(f'Enter element [{i}] [{j}]: '))
        row.append(ele)
    matrix1.append(row)

#Input second matrix
print('Enter elements of matrix2: ')
for i in range(m):
    row=[]
    for j in range(n):
        ele = int(input(f'Enter element [{i}] [{j}]: '))
        row.append(ele)
    matrix2.append(row)

#Display matrices in matrix form
def print_matrix(matrix):
    for row in matrix:
        print("".join(map(str, row)))

for i in range(m):
    row=[]
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)

print("\nMatrix1:")
print_matrix(matrix1)
print("\nMatrix2:")
print_matrix(matrix2)
print("\nMatrix3:")
print_matrix(matrix3)

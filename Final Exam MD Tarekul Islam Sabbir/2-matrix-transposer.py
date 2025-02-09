def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transposed_matrix = transpose(matrix)


print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
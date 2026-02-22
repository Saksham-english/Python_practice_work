# Wap to represent a matrix in the form of tuple . 
# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
matrix = []
print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert to tuple form
tuple_form = []
non_zero = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            tuple_form.append((i, j, matrix[i][j]))
            non_zero += 1

# Add first row (rows, columns, non-zero count)
tuple_form.insert(0, (rows, cols, non_zero))

# Display tuple form
print("\nTuple Form Representation:")
for item in tuple_form:
    print(item)

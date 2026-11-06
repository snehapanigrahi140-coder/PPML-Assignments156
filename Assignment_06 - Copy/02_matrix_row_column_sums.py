matrix = []
print("Enter 9 integers for a 3x3 matrix:")
for i in range(3):
    matrix.append([int(x) for x in input(f"Row {i+1}: ").split()])
for row in matrix:
    print(*row, "| Row sum:", sum(row))
print("Column sums:", [sum(matrix[r][c] for r in range(3)) for c in range(3)])

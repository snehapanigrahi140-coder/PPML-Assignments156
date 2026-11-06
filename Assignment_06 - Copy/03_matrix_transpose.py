rows = int(input("Rows: "))
cols = int(input("Columns: "))
matrix = [[int(input(f"Element [{r}][{c}]: ")) for c in range(cols)] for r in range(rows)]
print("Original matrix:")
for row in matrix: print(*row)
print("Transpose:")
for row in zip(*matrix): print(*row)

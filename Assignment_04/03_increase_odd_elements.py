values = [int(x) for x in input("Enter integers separated by spaces: ").split()]
for i in range(len(values)):
    if values[i] % 2 != 0:
        values[i] += 5
print(values)

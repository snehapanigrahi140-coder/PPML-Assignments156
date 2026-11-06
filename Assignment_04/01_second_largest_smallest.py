values = [int(input(f"Enter element {i+1}: ")) for i in range(10)]
unique = sorted(set(values))
if len(unique) < 2:
    print("Need at least two distinct values.")
else:
    print("Second smallest:", unique[1])
    print("Second largest:", unique[-2])

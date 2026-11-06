from collections import Counter
values = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
counts = Counter(values)
groups = [[value] * count for value, count in counts.items()]
print("Grouped matrix:", groups)

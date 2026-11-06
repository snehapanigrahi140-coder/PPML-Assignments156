list1 = [int(input(f"Integer {i+1}: ")) for i in range(5)]
list2 = [input(f"String {i+1}: ") for i in range(5)]
combined = []
for a, b in zip(list1, list2):
    combined.extend([a, b])
print(combined)

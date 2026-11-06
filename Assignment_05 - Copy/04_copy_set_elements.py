original = set(eval(input("Enter a set (example {1, 2, 3}): ")))
copied = set()
for item in original:
    copied.add(item)
print("Copied set:", copied)

d = eval(input("Enter dictionary (example {'a': 10, 'b': 20}): "))
if d:
    print("Key with maximum value:", max(d, key=d.get))
else:
    print("Dictionary is empty.")

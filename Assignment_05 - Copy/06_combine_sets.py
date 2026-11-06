s1 = set(eval(input("Enter first string set (example {'a', 'b'}): ")))
s2 = set(eval(input("Enter second string set (example {'b', 'c'}): ")))
combined = s1 | s2
print("Combined set without duplicates:", combined)

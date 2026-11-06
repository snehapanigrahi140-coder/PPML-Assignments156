d1 = eval(input("Enter first dictionary (example {'a': 1}): "))
d2 = eval(input("Enter second dictionary (example {'b': 2}): "))
d1.update(d2)
print("Merged dictionary:", d1)

d = eval(input("Enter dictionary (example {'a': 1, 'b': 1, 'c': 2}): "))
result = {}
seen = set()
for key, value in d.items():
    if value not in seen:
        result[key] = value
        seen.add(value)
print(result)

values = [int(x) for x in input("Enter integers: ").split()]
result = list(map(lambda x: x * 3, values))
print(result)

a1 = [int(x) for x in input("First array: ").split()]
a2 = [int(x) for x in input("Second array: ").split()]
common = list(filter(lambda x: x in a1, a2))
print("Intersection:", list(dict.fromkeys(common)))

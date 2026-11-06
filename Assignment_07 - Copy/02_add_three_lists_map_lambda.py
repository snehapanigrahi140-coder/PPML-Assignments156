a = [int(x) for x in input("List 1: ").split()]
b = [int(x) for x in input("List 2: ").split()]
c = [int(x) for x in input("List 3: ").split()]
if len(a) == len(b) == len(c):
    print(list(map(lambda x, y, z: x + y + z, a, b, c)))
else:
    print("All lists must have equal length.")

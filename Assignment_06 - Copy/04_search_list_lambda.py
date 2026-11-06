values = [int(x) for x in input("Enter list values separated by spaces: ").split()]
target = int(input("Element to search: "))
found = any(map(lambda x: x == target, values))
print("Element found" if found else "Element not found")

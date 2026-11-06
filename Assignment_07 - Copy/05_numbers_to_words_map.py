words = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
numbers = [int(x) for x in input("Enter digits (0-9): ").split()]
print(list(map(lambda n: words.get(n, "out of range"), numbers)))

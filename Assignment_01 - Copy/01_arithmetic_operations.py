x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
if y != 0:
    print("Division:", x / y)
    print("Remainder:", x % y)
    print("Floor division:", x // y)
else:
    print("Division, remainder and floor division are undefined when y is 0.")

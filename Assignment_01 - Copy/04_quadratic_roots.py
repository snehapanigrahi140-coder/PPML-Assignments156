import cmath
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == 0:
    print("This is not a quadratic equation.")
else:
    d = b*b - 4*a*c
    r1 = (-b + cmath.sqrt(d)) / (2*a)
    r2 = (-b - cmath.sqrt(d)) / (2*a)
    print("Roots:", r1, "and", r2)

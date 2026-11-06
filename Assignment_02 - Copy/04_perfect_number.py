n = int(input("Enter a positive integer: "))
total = sum(i for i in range(1, n) if n % i == 0)
print("Perfect number" if n > 0 and total == n else "Not a perfect number")

n = int(input("Enter an integer: "))
if n < 2:
    print("No prime factors.")
else:
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1: factors.append(n)
    print("Prime factors:", factors)

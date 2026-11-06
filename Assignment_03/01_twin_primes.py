n = int(input("Print twin primes up to: "))
def is_prime(x):
    if x < 2: return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))
for i in range(2, n - 1):
    if is_prime(i) and is_prime(i + 2):
        print((i, i + 2))

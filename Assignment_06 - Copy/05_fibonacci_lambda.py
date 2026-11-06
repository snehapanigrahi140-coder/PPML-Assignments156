from functools import reduce
n = int(input("Number of terms: "))
series = reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(max(0, n-2)), [0, 1]) if n >= 2 else ([0] if n == 1 else [])
print("Fibonacci series:", series[:n])

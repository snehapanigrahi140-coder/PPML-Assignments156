def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
terms = int(input("Number of terms: "))
fibonacci(terms)

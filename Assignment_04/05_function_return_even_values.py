def even_values(numbers):
    return [x for x in numbers if x % 2 == 0]
values = [int(x) for x in input("Enter integers separated by spaces: ").split()]
print("Even values:", even_values(values))

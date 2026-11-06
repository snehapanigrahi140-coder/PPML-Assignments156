bases = [int(x) for x in input("Enter bases: ").split()]
powers = [int(x) for x in input("Enter corresponding powers: ").split()]
if len(bases) == len(powers):
    print(list(map(pow, bases, powers)))
else:
    print("Both lists must have equal length.")

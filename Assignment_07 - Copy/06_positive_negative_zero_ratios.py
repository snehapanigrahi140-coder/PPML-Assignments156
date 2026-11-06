values = [int(x) for x in input("Enter integers: ").split()]
if not values:
    print("List is empty.")
else:
    total = len(values)
    ratios = list(map(lambda count: round(count / total, 2),
                      [sum(x > 0 for x in values), sum(x < 0 for x in values), sum(x == 0 for x in values)]))
    print("Ratios [positive, negative, zero]:", ratios)

meters = int(input("Distance in meters: "))
km, remaining_m = divmod(meters, 1000)
print(km, "kilometer(s)", remaining_m, "meter(s)")

minutes = int(input("Enter time in minutes: "))
hours, remaining_minutes = divmod(minutes, 60)
print(hours, "hour(s)", remaining_minutes, "minute(s)")

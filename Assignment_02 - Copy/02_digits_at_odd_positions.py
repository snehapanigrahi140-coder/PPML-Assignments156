n = input("Enter a 5-digit number: ")
if not n.isdigit() or len(n) != 5:
    print("Please enter exactly 5 digits.")
else:
    print("Digits at odd positions:", n[0], n[2], n[4])

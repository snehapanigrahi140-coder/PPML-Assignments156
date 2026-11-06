s = input("Enter a string: ")
clean = ''.join(ch.lower() for ch in s if ch.isalnum())
print("Palindrome" if clean == clean[::-1] else "Not a palindrome")

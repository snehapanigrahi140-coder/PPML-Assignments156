chars = input("Enter characters: ").split()
converted = list(map(lambda ch: ch.lower() if ch.isupper() else ch.upper(), chars))
print("Converted unique characters:", list(dict.fromkeys(converted)))

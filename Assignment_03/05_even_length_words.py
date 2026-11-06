s = input("Enter a sentence: ")
for word in s.split():
    if len(word) % 2 == 0:
        print(word)

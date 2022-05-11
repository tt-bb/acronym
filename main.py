sentence = input("Enter your sentence > ")

for char in sentence.title():
    if char.isupper():
        print(char, end="")
print()

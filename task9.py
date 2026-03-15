text = input("Введіть в рядок речення: ")

words = text.split()

for word in words:
    if word.lower().startswith("с"):
        print(word)
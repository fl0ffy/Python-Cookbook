"""Module for pyglatin exercise"""

PYG = "ay"
original = input("Enter a word:")


if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    new_word = word + first + PYG
    new_word = new_word[1 : len(new_word)]
    print(new_word)
else:
    print("empty")

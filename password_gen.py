# Password Generator:

import random
import string


def password_gen(length, lowercase=True, uppercase=True, digit=True, special_char=True):

    character = " "
    if lowercase:
        character += string.ascii_lowercase
    if uppercase:
        character += string.ascii_uppercase
    if digit:
        character += string.digits
    if special_char:
        character += string.punctuation

    password = " ".join(random.choice(character) for char in range(length))
    return password


print("Choose the level of complexity of the password")
print()
print("1. Easy")
print("2. Normal")
print("3. Hard")
print()

while True:
    choice = int(input("Enter the complexity level: "))

    if choice in (1, 2, 3):
        length = int(input("Enter the length of the password required: "))

        if choice == 1:
            password = password_gen(
                length, lowercase=True, uppercase=True, digit=False, special_char=False)
            print("Generated password:", password)

        elif choice == 2:
            password = password_gen(
                length, lowercase=True, uppercase=True, digit=True, special_char=False)
            print("Generated password:", password)

        elif choice == 3:
            password = password_gen(
                length, lowercase=True, uppercase=True, digit=True, special_char=True)
            print("Generated password:", password)
        break

    else:
        print("Choose a Valid Input")

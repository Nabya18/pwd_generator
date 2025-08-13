import random
import string

def generate_password(min_Lenght, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd

min_lenght = int(input("Minimum password length: "))
has_numbers = input("Do you have numbers? (y/n): ").lower() == "y"
has_special = input("Do you have special characters? (y/n): ").lower() == "y"
pwd = generate_password(min_lenght, has_numbers, has_special)
print(f"Your password is: {pwd}")
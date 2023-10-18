import string
import secrets


def generate_password(length: int, symbols: bool, uppercase: bool): 
    combination = string.ascii_lowercase + string.ascii_uppercase + string.digits

    if symbols:
        combination += string.punctuation

    if combination.isupper():
        combination += string.ascii_lowercase

        combination_length =len(combination)

        new_password = ""


        for _ in range(length):
            new_password += combination[secrets.randbelow(combination_length)]

            return new_password
        
        for _, index in enumerate(range(12)):
             Index = ":", generate_password (length, symbols, uppercase)
             print(index) + 1, ":", generate_password(length=30, symbols=True), uppercase=True)
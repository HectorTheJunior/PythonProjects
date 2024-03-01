import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


"""Here you can change the length and things like containing symbols or uppercase letters in password.
Also here it generate 3 passwords. There is always an option to change that too."""

for i in range(1, 4):
    new_pass: str = generate_password(length=12, symbols=True, uppercase=True)
    print(f"{i} -> {new_pass}  (U: {contains_upper(new_pass)}  S: {contains_symbols(new_pass)})")

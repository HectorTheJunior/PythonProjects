def password_checker(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_passwords in enumerate(common_passwords, start=1):
        if password == common_passwords:
            print(f'{password}: ❌(#{i})')
            return
    print(f'{password}: 👍(Unique)')


def main():
    user_password: str = input('Enter your password: \n')
    password_checker(user_password)


main()

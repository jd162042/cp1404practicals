"""Password Reader"""

# imports
# CONSTANTS

def main():
    min_password_length = 7

    print(f"Minimum password length is {min_password_length} characters")

    user_password = get_password(min_password_length)

    print_password(user_password)


def print_password(user_password: str):
    print(f"Your password is: {len(user_password) * "*"}")


def get_password(min_password_length: int) -> str:
    user_password = input("Enter password: ")
    while len(user_password) <= min_password_length:
        print("Error - set longer password")
        user_password = input("Enter password: ")
    return user_password


main()


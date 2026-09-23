"""Password Reader"""

min_password_length = 7

print(f"Minimum password length is {str(min_password_length)} characters")

user_password = input("Enter password: ")
while len(user_password) <= min_password_length:
    print("Error - set longer password")
    user_password = input("Enter password: ")

print(f"Your password is: {len(user_password) * "*"}")
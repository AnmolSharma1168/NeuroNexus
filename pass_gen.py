import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))

    print(f"Generated Password: {password}")


try:
    user_input = int(input("Enter desired password length: "))
    generate_password(user_input)
except ValueError:
    print("Please enter a valid number.")

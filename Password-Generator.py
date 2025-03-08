import random
import string

def generate_password(length):
    """Generate a secure random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length > 0:
                return length
            print("Length must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

length = get_password_length()
print("Generated Password:", generate_password(length))

import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")
    
    # Define possible characters for the password
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one of each required character type
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one special character
    ]
    
    # Fill the rest of the password with random characters
    password += random.choices(all_chars, k=length-4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Join the list into a single string and return
    return ''.join(password)

# Ask the user for the desired password length
length = int(input("Enter the desired password length (minimum 8 characters): "))
try:
    password = generate_password(length)
    print(f"Generated password: {password}")
except ValueError as e:
    print(e)

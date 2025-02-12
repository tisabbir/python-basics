import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")
    
   
    all_chars = string.ascii_letters + string.digits + string.punctuation
    

    password = [
        random.choice(string.ascii_uppercase), 
        random.choice(string.ascii_lowercase), 
        random.choice(string.digits),           
        random.choice(string.punctuation)      
    ]
    

    password += random.choices(all_chars, k=length-4)
    

    random.shuffle(password)
    

    return ''.join(password)

length = int(input("Enter the desired password length (minimum 8 characters): "))
try:
    password = generate_password(length)
    print(f"Generated password: {password}")
except ValueError as e:
    print(e)

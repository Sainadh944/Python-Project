import random
import string

def generate_password(length):
    if length<4:
        return "Password length should be atleast 4 characters."
    
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation

    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars=lowercase+uppercase+digits+symbols

    password+=random.choices(all_chars,k=length-4)

    random.shuffle(password)

    return ''.join(password)

length=int(input("Enter desired password length: "))
print("Generated Password: ",generate_password(length))
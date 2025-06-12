import random
import string

def generate_pswd(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
password = generate_pswd(length)
print("Your generated password is:", password)

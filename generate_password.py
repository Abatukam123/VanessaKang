import string
import random

def ran(): 
    all_characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        length = int(input("Enter the length of the password : "))
        if length >= 8:
            break
        else:
            print("Bad length. Please enter a length of 8 or higher.")

    password = ''.join(random.choices(all_characters, k=length))
    print("Your password is:", password)
    return password
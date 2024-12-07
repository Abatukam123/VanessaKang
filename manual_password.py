import re

def man():
    while True:
        pas = input("Enter your password: ")
        if len(pas) < 8:
            print("Password is too short. Must be at least 8 characters.")
        elif len(re.findall("[A-Z]", pas)) < 1:
            print("Password must contain at least one uppercase letter.")
        elif len(re.findall("[0-9]", pas)) < 1:
            print("Password must contain at least one digit.")
        elif len(re.findall("[!@#$%^&*()]", pas)) < 1:
            print("Password must contain at least one special character.")
        else:
            print("Your password is:", pas)
            break
    return pas
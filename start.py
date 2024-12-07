from cryptography.fernet import Fernet 
import os

def generate_key():
        if os.path.exists("encoding.txt"):
            with open("encoding.txt", "rb") as file:
                key = file.readline()
        else:
            key = Fernet.generate_key()
            with open("encoding.txt", "wb") as file:
                file.write(key)
        return key
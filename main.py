import getpass
import json
import logging
import generate_password
import manual_password
import start
from cryptography.fernet import Fernet 
import os

logging.basicConfig(filename="user_interaction.txt", level=logging.INFO, format="%(asctime)s : %(message)s")

class Functionalities:
    def create_credential(self, web, user, passw):
        print(web, user, passw)

class PasswordManagement(Functionalities):
    def __init__(self):
        self.Thekey = start.generate_key()

    def initializing(self):
        if os.path.exists("master_password.txt"):
            print("Anitialing system...")
            for x in range(3):
                login_password = getpass.getpass("Enter your password: ")
                with open("master_password.txt", "rb") as file:
                    password = file.readline()
                    decrypt_key = Fernet(self.Thekey).decrypt(password).decode()
                if login_password == decrypt_key:
                    logging.info("login in system.")
                    print("login in system...")
                    break
                else:
                    print("Wrong password.")
        else:
            print("Anitialing system...")
            master_password = getpass.getpass("Let create your login password: ")
            confirm_password = getpass.getpass("Confirm your login password: ")
            if master_password == confirm_password:
                encrypt_key = Fernet(self.Thekey).encrypt(master_password.encode())
                with open("master_password.txt", "wb") as file:
                    file.write(encrypt_key)
                logging.info("signing up the system")
                print("signing up system...")
            else:
                print("Passwords are mismatch.")
                exit()
    
    def log_acivities(self):
        try:
            with open("user_interaction.txt", "r") as file:
                text = file.read()
                print("\n" + text)
        except Exception as e:
            print("Error : " + str(e))



def main():
    all = PasswordManagement()
    all.initializing()
    while True:
        print("\n\n\n"+ " " * 56 + "Password Management System" + "\n\n\n")
        print("  " + "1. Create credencial")
        print("  " + "2. Retrieve password")
        print("  " + "3. Update password")
        print("  " + "4. Delete credencial")
        print("  " + "5. Show recent activities")
        print("  " + "6. Exit")
        user_input = input("Choose an option(1-6): ")
        if user_input == "1":
            website = input("Enter the name of the website: ")
            username = input("Enter you username: ")
            print("\n  " + "1. Manually password")
            print("  " + "2. Auto generated password\n")
            while True:
                choice = input("Enter your choice(1-2): ")
                if choice == "1":
                    passwrd = manual_password.man()
                    all.create_credential(website,username,passwrd)
                    logging.info("Creating credential: {}.".format(website))
                    break
                elif choice == "2":
                    passwrd = generate_password.ran()
                    all.create_credential(website,username,passwrd)
                    logging.info("Creating credential: {}.".format(website))
                    break
                else:
                    print("Enter a valid choice bro.")
        if user_input == "2":
            pass
        if user_input == "3":
            pass
        if user_input == "4":
            pass
        if user_input == "6":
            exit()
        if user_input == "5":
            all.log_acivities()

if __name__ == "__main__":
    main()


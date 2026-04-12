import pyperclip
import os 

FILE_NAME = "passwords.txt"

def save_password():
    website = input("Enter website: ")
    password = input("Enter password: ") 
    with open(FILE_NAME, "a") as f:
        f.write(f"{website}<||>{password}\n")

def get_password():
    if not os.path.exists(FILE_NAME):
        print("No passwords saved yet.")
        return
    
    website = input("Enter website: ")
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if website in line:
                parts = line.strip().split("<||>")
                if len(parts) == 2:
                    password = parts[1]
                    pyperclip.copy(password) 
                    print("Password copied to clipboard!")
                    found = True
                    break
    
    if not found:
        print("Website not found.")

def main():
    while True:
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            save_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
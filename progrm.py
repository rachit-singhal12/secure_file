from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("Secret.key","rb").read()

def encrypt(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename,"wb") as file:
        file.write(encrypted_data)

def decrypt(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except ImportError:
            print("invalid key")
            return
    with open(filename,"wb") as file:
        file.write(decrypted_data)
    
choice = input("enter e to encrypt the data press d to decrypt the data : \n").lower()

if choice == 'e':
    filename = input("enter the filename to encrypt (including the extension):\n")
    if os.path.exists(filename):
        generate_key()
        key = load_key()
        encrypt(filename,key)
        print("file encrypted successfully")
    else:
        print("invalid file name")

elif choice == 'd':
    filename = input("enter the filename to encrypt (including the extension): \n")
    if os.path.exists(filename):
        key = load_key()
        decrypt(filename,key)
        print("file decrypted successfully")
    else:
        print("invalid file name")

else:
    print("invalid choice") 
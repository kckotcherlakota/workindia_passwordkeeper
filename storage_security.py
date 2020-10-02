from cryptography.fernet import Fernet
import os 

""" class to encrypt and decrypt webiste passwords """
class StorageSecurity:

    
    def __init__(self):
        if os.path.exists("storage.key"):
            print("Reading Storage security key")
            with open('storage.key','rb') as key_file:
                key = key_file.read()
                self.suite = Fernet(key)
        else:
            print("Generating Storage security key")
            key = Fernet.generate_key()
            with open('storage.key','wb') as key_file:
                key_file.write(key)
                self.suite = Fernet(key)        
      

    
    def encrypt(self,password):
        byte_str = bytes(password,'utf-8')
        encrypted = self.suite.encrypt(byte_str)
        return encrypted

    
    def decrypt(self,encrypt):
        password = self.suite.decrypt(encrypt)
        password = password.decode('utf-8')
        return password 


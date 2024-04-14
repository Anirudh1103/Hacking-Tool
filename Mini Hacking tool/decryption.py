import base64
from cryptography.fernet import Fernet
with open('thekey.txt','r') as k:
    key = k.read()
    
f_object = Fernet(key)
with open('encrypted_text.txt','r') as e:
    encrypted_text = e.read()
    decrypted_text = f_object.decrypt(encrypted_text)
   



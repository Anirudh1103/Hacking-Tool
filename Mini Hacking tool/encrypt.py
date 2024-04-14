from cryptography.fernet import Fernet
import base64
key = Fernet.generate_key()

print("\t\t***** Welcome to Encrypter & Decrypter ******")
messsage = input('Enter the text you want to encrypt: \n').encode()
f_object = Fernet(key)
byte_key = key.encode('ascii')
base64_key = base64.b64encode(byte_key)
with open('thekey.txt','w') as k:
    k.write(byte_key)
    k.close()
encrypted_msg = f_object.encrypt(messsage)
with open('encrypted_text.txt', 'w') as f:
    f.write(str(encrypted_msg))
    f.close()
print('The encrypted message is stored in a file: encrypted_text.txt')
print('Key is stored in file                    :key.txt')
decrypted_msg = f_object.decrypt(encrypted_msg)
print('Decrypted message:\n',decrypted_msg)


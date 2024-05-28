from subprocess import call
import subprocess
from termcolor import colored
print(colored("\t\t\tWelcome to  HACKING  tool",'red',attrs=['blink']))
print(colored("\t\t\t\t\t\t ~ Anirudh C M",'red'))
print(colored("Disclaimer: Dont misuse this tool to steal others data without victim's permission..!!\n\n",'red'))

while True:
    print(colored('Below are the attacks this tool can perform...\n','green'))

    print(colored('1. Caesar Cipher Encryption & Decryption','green'))
    print(colored('2. Password List Generator','green'))
    print(colored('3. Hashed Password Cracker','green'))
    print(colored('4. PDF Password Cracker','green'))
    print(colored('5. Zip file Password Cracker','green'))
    print(colored('6. Steganography','green'))
    print(colored('7. Exit','green'))
    ch = int(input(colored('Enter your choice...\n','green')))

    match ch:
        case 1:
            call(['python','cipher_encrypt.py'])
        
        case 2:
            subprocess.run('/home/kali/Desktop/Hacking_Tool/cupp/cupp.py -i',shell=True)
        case 3:
            s = input("Enter the hashed string: ")
            subprocess.run('python hash.py -s ' + s,shell=True)
        case 4:
            call(['python','PDF_pwd.py'])
        case 5:
            call(['python','PDF_pwd.py'])
        case 6:
            call(['python','stegno.py'])
        case 7:
            print("Thank you for using " + colored("HACKING TOOL",'red'))
            print('Created by ',colored('ANIRUDH C M','green',attrs=['blink']))
            print('_'*94)
            break
  #Non hashed password cracker
#Zip file password cracker



import pikepdf
from termcolor import colored
import time

pdf_file = input('PDF: ')
password_list= input("PASSWORD_LIST: ")
passwords = open(password_list)

i=0
start_time = time.time()
for passsword in passwords:
    passsword = passsword.strip('\n')
    i += 1
    #print(colored("\r {} Password Tested ! ".format(i),'red'),end="")
    try:
        pikepdf.open(pdf_file, password=passsword)
        print(colored('\n' + '* ' *20 ,'red'))
        end_time = time.time()
        print(colored('Password Found! ','green'))
        print('PASSWORD: ',colored(passsword,'green',attrs=['blink']))
        print(colored('[{}] PASSWORD TESTED IN {} SECOND! '.format(i,str(end_time - start_time)[:4]),'red'))
        print(colored('* '*20,'red'))
        passwords.close()
        break
    except:
        print(colored('Trying Password: {}'.format(passsword),'red'))
        pass
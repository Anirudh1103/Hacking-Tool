from subprocess import call
from termcolor import colored
print(colored("\t\t\tWelcome to mini hacking tool\n\n",'red'))
print(colored('Disclaimer: Dont misuse me to steal others data without their permission..!!\n\n','red'))

while True:
    print(colored('Below are the tasks I can perform...\n','green'))

    print(colored('1. Encrypt','green'))
    print(colored('2. Decryption with key','green'))
    print(colored('3. Random password generator','green'))
    print(colored('4. Wifi password extractor','green'))
    print(colored('5. PDF password cracker','green'))
    print(colored('6. Zip file password cracker','green'))
    print(colored('7. Exit','green'))
    ch = int(input(colored('Enter your choice...\n','green')))

    match ch:
        case 1:
            call(['python','encrypt.py'])
        
        case 2:
            call(['python','decryption.py'])
        case 3:
            call(['python','pass_gen.py'])
        case 4:
            call(['python','wifi_pass.py'])
        case 5:
            call(['python','pdf_pass.py'])
        case 6:
            call(['python','zip_pass_cracker.py'])
        case 7:
            print("Thank you for using" + colored(" MINI HACKING TOOL",'red'))
            print('Created by ANIRUDH C M & CHANDAN T O ')
            exit()
    print('_'*100)
    




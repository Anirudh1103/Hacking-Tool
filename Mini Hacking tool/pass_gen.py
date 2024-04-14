import random
from termcolor import colored
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&+-"
len = int(input(colored('Enter the length of the password:  ','green')))
a = "".join(random.sample(password,len))
print(colored('Your pass is: ','green'),end="")
print(colored(a,'red'))
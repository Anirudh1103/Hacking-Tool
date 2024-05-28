import zipfile
def extractFile(zfile, password):
    try:
        zfile.extractall(pwd = bytes(password, 'utf-8'))
        return password
    except:
        print("Trying to crack the password....")
        return
def main():
    zfile = zipfile.ZipFile('demo.zip')
    passFile = open('rockyou.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile,password)
        if guess:
            print('Password = ' + password)
            break
if __name__ == 'main':
    main()
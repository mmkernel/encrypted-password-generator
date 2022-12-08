import random
from cryptography.fernet import Fernet
import os.path

# Check if path exist, if yes, decrypt the location and password
if os.path.exists('location'):
    with open('locationKey', 'rb') as lk:
        encryptLocation = lk.read()
    with open('location', 'rb') as decLoc:
        decLocation = decLoc.read()
    decryptLocation = Fernet(encryptLocation).decrypt(decLocation)
    with open('location', 'wb') as lo:
        lo.write(decryptLocation)
    with open('location', 'r') as loc:
        pathLocation = loc.read()
        if pathLocation.endswith("\\"):
            pass
        else:
            pathLocation = pathLocation + '\\'
    with open(pathLocation+'pass', 'r') as theFile:
        content = theFile.read()
    with open(pathLocation+'theKey', 'r') as theKey:
        encryptionKey = theKey.read()
    decryptPass = Fernet(encryptionKey).decrypt(content)
    with open(pathLocation+'pass', 'wb') as decPasswords:
        decPasswords.write(decryptPass)
# ..if not, enter the new path
# pass and theKey file will be created into new path
# location and locationKey will be created into app directory
else:
    path = input('Enter the full path: ')
    if path.endswith("\\"):
        pathPass = path + 'pass'
        pathKey = path + 'theKey'
        pathLocation = path
    else:
        pathPass = path + '\\pass'
        pathKey = path + '\\theKey'
        pathLocation = path + '\\'

    with open(pathPass, 'w') as thePass:
        thePass.write('')

    key = Fernet.generate_key()
    with open(pathKey, 'wb') as theKey:
        theKey.write(key)

    with open('location', 'w') as patLoc:
        patLoc.write(path)

    locKey = Fernet.generate_key()
    with open('locationKey', 'wb') as lk:
        lk.write(locKey)

print('*'*80)
print('PASSWORD GENERATOR & ENCRYPTOR'.center(80))
print('*'*80)

# Encrypt the location and pass file before exit
def encrypt():
    with open(pathLocation+'theKey', 'rb') as theKey:
        encryptionKey = theKey.read()
    with open(pathLocation+'pass', 'rb') as thefile:
        content = thefile.read()
    encryptPass = Fernet(encryptionKey).encrypt(content)
    with open(pathLocation+'pass', 'wb') as enc_passwords:
        enc_passwords.write(encryptPass)
    with open('locationKey', 'rb') as locationKey:
        locationKey = locationKey.read()
    with open('location', 'rb') as pL:
        pathLoc = pL.read()
    encryptLocation = Fernet(locationKey).encrypt(pathLoc)
    with open('location', 'wb') as enc_location:
        enc_location.write(encryptLocation)

# Generate new complex 16 characters long passwords
def newPass():
    lower = 'qwertzuiopasdfghjklyxcvbnm'
    upper = 'QWERTZUIOPASDFGHJKLYXCVBNM'
    numbers = '0123456789'
    signs = '!$%&^().=*-{[]}'
    string = lower + upper + numbers + signs
    length = 16
    password = "".join(random.sample(string,length))
    return password

def startPage():
    print('-'*80)
    action = input('''[1] - GENERATE AND SAVE NEW PASSWORD
[2] - ENTER MANUALLY NEW PASSWORDS
[3] - VIEW SAVED PASSWORDS
[4] - ENCRYPT PASSWORDS AND EXIT
''')
    print('-'*80)

    if action == '1':
        print('Your new password:',newPass())
        alias = input('Alias for new password (Website, Username..): ')
        with open(pathLocation+'pass', 'a') as f:
            f.write(f'{alias}: {newPass()}\n')
    elif action == '2':
        mPass = input('Enter your new password: ')
        alias = input('Alias for new password (Website, Username..): ')
        with open(pathLocation+'pass', 'a') as f:
            f.write(f'{alias}: {mPass}\n')
    elif action == '3':
        with open(pathLocation+'pass', 'r') as f:
            print(f.read())
    elif action == '4':
        encrypt()
        quit()


while True:
    startPage()


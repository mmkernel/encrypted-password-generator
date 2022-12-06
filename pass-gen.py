import random
from cryptography.fernet import Fernet
import os.path

print('*'*80)
print('PASSWORD GENERATOR & ENCRYPTOR'.center(80))
print('*'*80)


# Generate Encryption Key
def keyGenerator():
    key = Fernet.generate_key()
    with open('theKey', 'wb') as theKey:
        theKey.write(key)
# Create backup key in case you lost theKey
    with open('backupKey', 'wb') as backupKey:
        backupKey.write(key)
        os.system("attrib +h backupKey")

# Check if the encrypted file exists
# if so, decrypt the passwords file
if os.path.exists('theKey'):
    with open('theKey', 'rb') as theKey:
        encryptionKey = theKey.read()
    with open('pass', 'rb') as thefile:
        content = thefile.read()
    decryptPass = Fernet(encryptionKey).decrypt(content)
    with open('pass', 'wb') as dec_passwords:
        dec_passwords.write(decryptPass)
else: keyGenerator()

# Generate new password
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
        with open('pass', 'a') as f:
            f.write(f'{alias}: {newPass()}\n')
    elif action == '2':
        mPass = input('Enter your new password: ')
        alias = input('Alias for new password (Website, Username..): ')
        with open('pass', 'a') as f:
            f.write(f'{alias}: {mPass}\n')
    elif action == '3':
        with open('pass', 'r') as f:
            print(f.read())
    elif action == '4':
        with open('theKey', 'rb') as theKey:
            encryptionKey = theKey.read()
        with open('pass', 'rb') as thefile:
            content = thefile.read()
        encryptPass = Fernet(encryptionKey).encrypt(content)
        with open('pass', 'wb') as enc_passwords:
            enc_passwords.write(encryptPass)
        quit()


while True:
    startPage()


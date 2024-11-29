import random
import math

def menu():
    while True:
        choice = int(input('''
    Welcome, here are your options, please select a number:
        1. Encrypt a message
        2. Decrypt a message
        3. Quit \n\n'''))
        if choice == 1:
            text_file()
            encryption_key()
            encrypt(text_file(), offset_factor(encryption_key()))
        elif choice == 2:
            decrypt()
        elif choice == 3:
            exit('Au revior!')
        else:
            print('Invalid input try again')

def text_file():
    file = open('Cipher Text/sample.txt','r')
    file1 = (file.read())
    print(file1)
    return file1

def encryption_key():
    key = []
    for i in range(0, 8):
        rand_int = random.randint(34, 125)
        key.append(ascii(rand_int))
    print("You're key is: ", key)
    return rand_int
    
def offset_factor(nums):
    total = 0
    for i in range(0, 8):
        total += nums
    offset = ((math.floor(total / 8))-32)
    return(offset)

def encrypt(msg, offset_factor):
    encrypted = []
    for i in msg:
        if i != ' ':
            i = ord(i) + offset_factor
            if i > 126:
                i -= 94
            i = chr(i)
            encrypted.append(i)
        else:
            continue
    encrypted = " ".join(str(x) for x in encrypted)
    print(encrypted)
    
#----------main-------------------

menu()
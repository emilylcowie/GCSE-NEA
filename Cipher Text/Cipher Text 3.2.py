import random

def menu():
    while True:
        choice = int(input('''
    Welcome, here are your options, please select a number:
        1. Encrypt a message
        2. Decrypt a message
        3. Quit \n\n'''))
        if choice == 1:
            text_file()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            exit('Au revior!')
        else:
            print('Invalid input try again')

def text_file():
    file = open('Cipher Text/sample.txt','r')
    print(file.read())
    encryption_key()

def encryption_key():
    key = []
    total = 0
    for i in range(0, 8):
        rand_int = random.randint(34, 125)
        key.append(ascii(rand_int))
        total += rand_int
    print("You're key is: ", key)
    print("total: ", total)
#
menu()
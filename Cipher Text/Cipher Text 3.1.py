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
    user_message = input('What is the name of the .txt file containing the message to be encrypted?\n')
    file = open('/workspaces/GCSE-NEA/Cipher Text/'+user_message, 'r')
    print(file.read())
    encryption_key()

def encryption_key():
    key = []
    for i in range(0, 8):
        rand_int = random.randint(34, 125)
        key.append(ascii(rand_int))
        total += i
    print("You're key is: ", key)
    print("total: ", total)

menu()
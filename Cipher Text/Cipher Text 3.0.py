import random
for i in range(33, 126):
    print(random.randint(33,126))

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
    user_message = input('What is the name of the .txt file containing the message to be encrypted?')
    with open(user_message, 'r') as file:
        content = file.read()
    encrypt()

def encrypt():
    rand_int = random.randint(33, 126)
with open('Cipher Text/sample.txt', 'r') as file:
    content = file.read()

def menu():
    choice = input('''
Welcome, here are your options, please select a number:
    1. Encrypt a message
    2. Decrypt a message
    3. Quit \n\n''')


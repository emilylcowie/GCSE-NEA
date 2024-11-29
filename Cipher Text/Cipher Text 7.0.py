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
            message = text_file()
            key = encryption_key()
            offset = offset_factor(key)
            encrypt(message, offset)
        elif choice == 2:
            decrypt_admin()
        elif choice == 3:
            exit('Au revoir!')
        else:
            print('Invalid input, try again.')

def text_file():
    # get file name and read it
    filename = input('File name:\n')
    with open(f'Cipher Text/{filename}.txt', 'r') as file:
        file_content = file.read()
    return file_content

def encryption_key():
    # make random encryption key
    key = []
    for _ in range(8):
        rand_int = random.randint(34, 125)
        key.append(chr(rand_int))
    key = "".join(key)
    print("Your key is:", key)
    return key

def offset_factor(key):
    # make offset factor from the encryption key
    total = sum(ord(char) for char in key)
    offset = (math.floor(total / 8)) - 32
    return offset

def encrypt(msg, offset_factor):
    # encrypt message with offset factor
    encrypted = []
    for char in msg:
        if char != ' ':
            encrypted_char = ord(char) + offset_factor
            if encrypted_char > 126:
                encrypted_char -= 94
            encrypted_char = chr(encrypted_char)
            encrypted.append(encrypted_char)
        else:
            encrypted.append(' ')

    encrypted_message = "".join(encrypted)
    save(encrypted_message)

def save(encrypted_msg):
    filename = input("New file name:\n")
    with open(f'Cipher Text/{filename}.txt', "x") as file:
        file.write(encrypted_msg)

def decrypt_admin():
    """Decrypt the message using the provided key."""
    file_content = text_file()
    decryption_key = input('Encryption key:\n')
    offset_value = offset_factor(decryption_key)
    decrypted = []

    for char in file_content:
        if char != ' ':
            decrypted_char = ord(char) - offset_value  # Subtract offset during decryption
            if decrypted_char < 32:
                decrypted_char += 94  # Wrap around to maintain printable ASCII characters
            decrypted_char = chr(decrypted_char)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(' ')  # Preserve spaces during decryption

    decrypted_message = "".join(decrypted)  # Join without additional spaces
    print("Decrypted Message:", decrypted_message)

# Main 
menu()

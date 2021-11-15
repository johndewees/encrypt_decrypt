import random
import fnmatch
from datetime import datetime

#-------------------------------------------------------
# variable storage warehouse
# chars_ordered_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
# chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?0123456789 '
#-------------------------------------------------------

# TODO: Add print statements to confirm command actions to each of the functions to provide user feedback

# Function to create a cypher if one does not previously exist
# Creates cypher in new text file
def create_cypher():
    cypher_file_name = input('What would you like your cypher to be named?  ')
    cypher_file_name = cypher_file_name + '_cypher.txt'
    chars_shuffle_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    random.shuffle(chars_shuffle_lis)
    chars_shuffle_str = ''
    for char in chars_shuffle_lis:
        chars_shuffle_str += char
    cypherhand = open(cypher_file_name, "w")
    cypherhand.write(chars_shuffle_str)
    cypherhand.close()
    print('\n* Your cypher has been created *\n')

# Function to take a plaintext message and encrypt it with a cypher.txt file
def encrypt_message():
    message_file_name = input('What is the name of the file? (Must be ".txt")')
    message_file_name = message_file_name + '.txt'
    chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?0123456789 '
    pmhand = open(message_file_name, "r")
    message_string = pmhand.read()
    message_text = message_string.splitlines()
    cypherhand = open("cypher.txt", "r")
    cypher = cypherhand.read()
    cmhand = open("cypher_message.txt", "w")
    cypher_text_list = []
    for line in message_text:
        cypher_line = ''
        for char in line:
            if char in chars_ordered_str:
                pos = chars_ordered_str.find(char)
                cypher_char = char.replace(chars_ordered_str[pos], cypher[pos])
                cypher_line += cypher_char
        cypher_text_list.append(cypher_line)
    cypher_text_str = ''
    for line in cypher_text_list:
        if line == '':
            cypher_text_str = cypher_text_str + '\n'
        elif line == cypher_text_list[-1]:
            cypher_text_str = cypher_text_str + line
        else:
            cypher_text_str = cypher_text_str + line + '\n'
    cmhand.write(cypher_text_str)
    cmhand.close()
    pmhand.close()
    cypherhand.close()
    print('\n* Your message has been encoded with the cypher *\n')

# Function to take a cyphertext message and decrypt it with a cypher.txt file
# This appends the plain text message after the cyphertext in the same cypher.txt file
def decrypt_message():
    chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?0123456789 '
    cmhand = open('cypher_message.txt', 'r')
    cypher_string = cmhand.read()
    cypher_text = cypher_string.splitlines()
    cypherhand = open("cypher.txt", "r")
    cypher = cypherhand.read()
    plain_text_list = []
    for line in cypher_text:
        plain_line = ''
        for char in line:
            if char in cypher:
                pos = cypher.find(char)
                plain_char = char.replace(cypher[pos], chars_ordered_str[pos])
                plain_line += plain_char
        plain_text_list.append(plain_line)
    plain_text_str = '\n\n-------------------------------\nYOUR DECRYPTED MESSAGE IS BELOW\n-------------------------------\n\n'
    for line in plain_text_list:
        if line == '':
            plain_text_str = plain_text_str + '\n'
        elif line == plain_text_list[-1]:
            plain_text_str = plain_text_str + line
        else:
            plain_text_str = plain_text_str + line + '\n'
    cmhand.close()
    cmhand = open('cypher_message.txt', 'a')
    cmhand.write(plain_text_str)
    cmhand.close()
    cypherhand.close()
    print('\n* Your message has been decoded with the cypher and appended to your encrypted message file *\n')

def help():
    print('''
    1. Create a cypher by which you can encode and decode plaintext messages
        To create a new cypher enter the command: 'CYPHER'
    2. Encode a previously existing message with an existing cypher
        To encode a plaintext message with a cypher enter the command: 'ENCODE'
    3. Decode an encoded message so long as you have the corresponding cypher
        To decode a cyphertext message with a cypher enter the command: 'DECODE'
    
    To exit this program enter the command: 'EXIT'

    *Note: All files must be in the same directory as encrypt_decrypt.py
    *Note: All commands must be entered exactly (minus the single quotes) and are case-sensitive
    *Note: Whenever a filename is requested, there is no need to include the file extension
    ''')

print('''
    GREETINGS SPYMASTER!!!
    This program allows you to:
    1. Create a cypher by which you can encode and decode plaintext messages
        To create a new cypher enter the command: 'CYPHER'
    2. Encode a previously existing message with an existing cypher
        To encode a plaintext message with a cypher enter the command: 'ENCODE'
    3. Decode an encoded message so long as you have the corresponding cypher
        To decode a cyphertext message with a cypher enter the command: 'DECODE'
    
    To exit this program enter the command: 'EXIT'
    To view these options again enter the command: 'HELP

    *Note: All files must be in the same directory as encrypt_decrypt.py
    *Note: All commands must be entered exactly (minus the single quotes) and are case-sensitive
    *Note: Whenever a filename is requested, there is no need to include the file extension
''')

user_choice = ''
while user_choice != 'EXIT':
    user_choice = input('COMMAND:  ')
    if user_choice == 'CYPHER':
        create_cypher()
    elif user_choice == 'ENCODE':
        encrypt_message()
    elif user_choice == 'DECODE':
        decrypt_message()
    elif user_choice == 'HELP':
        help()
    elif user_choice == 'EXIT':
        print('GO FORTH SPYMASTER!')
    else:
        print("I don't understand your COMMAND, please try again")
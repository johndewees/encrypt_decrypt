import random
import pyperclip
from datetime import datetime

# The asterisk ("*") is a controlled character in this program and may not be used in the substitution cypher and should not be used in message texts

#-------------------------------------------------------
# variable storage warehouse
# chars_ordered_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
# chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?-0123456789 '
#-------------------------------------------------------

# Function to create a cypher if one does not previously exist
# Creates cypher in new text file
def create_cypher():
    today = datetime.today()
    cypher_file_name = today.strftime("%Y-%m-%d %H%M%S")
    chars_shuffle_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    random.shuffle(chars_shuffle_lis)
    chars_shuffle_str = ''
    for char in chars_shuffle_lis:
        chars_shuffle_str += char
    cypherhand = open(cypher_file_name + '_cypher.txt', "w")
    cypherhand.write(chars_shuffle_str)
    cypherhand.close()
    cypher_file_name = cypher_file_name + '_cypher'
    pyperclip.copy(cypher_file_name)
    print('The filename of the cypher is: ',cypher_file_name)
    print('The filename has been copied to the clipboard')
    print('* Your cypher has been created *\n')

# Function to write a plaintext message in the encrypt_decrypt.py program itself and encrypt it with a cypher.txt file
def write_message():
    print('''Let's encode a short message
    You will (1) write the message,
    (2) provide the filename of the cypher used to encrypt it,
    and (3) provide the filename you would like your newly encrypted text message to be called,
    in that order.''')
    message_text_input = input('Please write the message you would like to encrypt.\n')
    cypher_input = input('Please enter the filename of the cypher you would like to encrypt the message.\n')
    cypherhand = open(cypher_input + ".txt", "r")
    cypher = cypherhand.read()
    cypher_message = input('What would you like to call the file containing the encoded message?\n')
    cmhand = open(cypher_message + ".txt", "w")
    chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?-0123456789 '
    message_text = message_text_input.splitlines()
    today = datetime.today()
    today_str = today.strftime("%Y-%m-%d %H%M%S")
    today_str_enc = ''
    for char in today_str:
        if char in chars_ordered_str:
            pos = chars_ordered_str.find(char)
            today_char = char.replace(chars_ordered_str[pos], cypher[pos])
            today_str_enc += today_char
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
    cypher_text_str = cypher_text_str + '\n' + today_str_enc
    cmhand.write(cypher_text_str)
    cmhand.close()
    cypherhand.close()
    print('* Your message has been encoded with the cypher *\n')

# Function to take a plaintext message and encrypt it with a cypher.txt file
def encrypt_message():
    print('''Let's encode a pre-existing text file
    You will (1) provide the file name, and
    (2) provide the filename of the cypher used to encrypt it,
    in that order.''')
    message_file_name = input('What is the name of the file? (Must be ".txt")\n')
    message_hand = open(message_file_name + '.txt', "r")
    message_string = message_hand.read()
    message_hand.close()
    message_text = message_string.splitlines()
    cypher_input = input('Please enter the filename of the cypher you would like to encrypt the message.\n')
    cypherhand = open(cypher_input + ".txt", "r")
    cypher = cypherhand.read()
    cypher_text_list = []
    chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?-0123456789 '
    today = datetime.today()
    today_str = today.strftime("%Y-%m-%d %H%M%S")
    today_str_enc = ''
    for char in today_str:
        if char in chars_ordered_str:
            pos = chars_ordered_str.find(char)
            today_char = char.replace(chars_ordered_str[pos], cypher[pos])
            today_str_enc += today_char
    for line in message_text:
        if line.startswith('*'):
            cypher_text_list.append(line)
        else:
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
    cypher_text_str = cypher_text_str + '\n' + today_str_enc
    message_hand = open(message_file_name + '.txt', "w")
    message_hand.write(cypher_text_str)
    message_hand.close()
    cypherhand.close()
    print('* Your message has been encoded with the cypher *\n')

# Function to take a cyphertext message and decrypt it with a cypher.txt file
# This appends the plain text message after the cyphertext in the same cypher.txt file
def decrypt_message():
    print('''Let's decode a message
    You will (1) provide the name of the file to decrypt and
    (2) provide the filename of the cypher used to encrypt it,
    in that order. The decoded message will appear after the encoded message''')
    message_file_name = input('What is the name of the file? (Must be ".txt")\n')
    chars_ordered_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.!?-0123456789 '
    message_hand = open(message_file_name + '.txt', 'r')
    cypher_string = message_hand.read()
    message_hand.close()
    cypher_text = cypher_string.splitlines()
    cypher_input = input('Please enter the filename of the cypher you would like to decrypt the message.\n')
    cypherhand = open(cypher_input + ".txt", "r")
    cypher = cypherhand.read()
    cypherhand.close()
    star_text_list = []
    encoded_text_list = []
    plain_text_list = []
    section_break = '*\n*------------------------------------------------\n*\n'
    for line in cypher_text:
        if line.startswith('*'):
            star_text_list.append(line)
        else:
            plain_line = ''
            for char in line:
                if char in cypher:
                    pos = cypher.find(char)
                    plain_char = char.replace(cypher[pos], chars_ordered_str[pos])
                    plain_line += plain_char
            plain_text_list.append(plain_line)
            encoded_text_list.append('* ' + line)
    star_text_str = ''
    for line in star_text_list:
        if line == '':
            star_text_str = star_text_str + '\n'
        elif line == plain_text_list[-1]:
            star_text_str = star_text_str + line
        else:
            star_text_str = star_text_str + line + '\n'
    code_text_str = ''
    for line in encoded_text_list:
        if line == '':
            code_text_str = code_text_str + '\n'
        elif line == plain_text_list[-1]:
            code_text_str = code_text_str + line
        else:
            code_text_str = code_text_str + line + '\n'
    plain_text_str = ''
    for line in plain_text_list:
        if line == '':
            plain_text_str = plain_text_str + '\n'
        elif line == plain_text_list[-1]:
            plain_text_str = plain_text_str + line
        else:
            plain_text_str = plain_text_str + line + '\n'
    new_file_contents = ''
    if len(star_text_list) == 0:
        new_file_contents = code_text_str + section_break + plain_text_str
    else:
        new_file_contents = star_text_str + code_text_str + section_break + plain_text_str    
    message_hand = open(message_file_name + '.txt', 'w')
    message_hand.write(new_file_contents)
    message_hand.close()
    print('* Your message has been decoded with the cypher and appended to your encrypted message file *\n')

def help():
    print('''
    1. Create a cypher by which you can encode and decode plaintext messages
        To create a new cypher enter the command: 'CYPHER'
    2. Quickly write an encoded message with an existing cypher in the program
        To write a message in the command line enter the command: 'WRITE'
    3. Encode a previously existing message with an existing cypher
        To encode a plaintext message with a cypher enter the command: 'ENCODE'
    4. Decode an encoded message so long as you have the corresponding cypher
        To decode a cyphertext message with a cypher enter the command: 'DECODE'
    
    To exit this program enter the command: 'EXIT'

    *Note: All files must be in the same directory as encrypt_decrypt.py
    *Note: All commands must be entered exactly (minus the single quotes) and are case-sensitive
    *Note: Whenever a filename is requested, there is no need to include the file extension
    *Note: The asterisk ("*") may not be used in the text of messages
    ''')

print('''
    GREETINGS SPYMASTER!!!
    This program allows you to:
    1. Create a cypher by which you can encode and decode plaintext messages
        To create a new cypher enter the command: 'CYPHER'
    2. Quickly write an encoded message with an existing cypher in the program
        To write a message in the command line enter the command: 'WRITE'
    3. Encode a previously existing message with an existing cypher
        To encode a plaintext message with a cypher enter the command: 'ENCODE'
    4. Decode an encoded message so long as you have the corresponding cypher
        To decode a cyphertext message with a cypher enter the command: 'DECODE'
    
    To exit this program enter the command: 'EXIT'
    To view these options again enter the command: 'HELP

    *Note: All files must be in the same directory as encrypt_decrypt.py
    *Note: All commands must be entered exactly (minus the single quotes) and are case-sensitive
    *Note: Whenever a filename is requested, there is no need to include the file extension
    *Note: The asterisk ("*") may not be used in the text of messages
''')

user_choice = ''
while user_choice != 'EXIT':
    user_choice = input('COMMAND:  ')
    if user_choice == 'CYPHER':
        create_cypher()
    elif user_choice == 'WRITE':
        write_message()
    elif user_choice == 'ENCODE':
        encrypt_message()
    elif user_choice == 'DECODE':
        decrypt_message()
    elif user_choice == 'HELP':
        help()
    elif user_choice == 'EXIT':
        print('\nGO FORTH SPYMASTER!\n')
    else:
        print("I don't understand your COMMAND, please try again\n")

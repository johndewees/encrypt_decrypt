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
    print('''You can create a cypher of varying complexity
    To create a single-substitution cypher,
        (every character in the message is replace by a single random character)
        enter the command: 'SINGLE'
    To create a double-substitution cypher,
        (every character in the message is replace by a random two character string)
        enter the command: 'DOUBLE'
    To create a single-substitution cypher,
        (every character in the message is replace by a random three character string)
        enter the command: 'TRIPLE'
    ''')
    user_choice = input('COMMAND:  ')
    cypher_type = 0
    if user_choice == 'SINGLE':
        cypher_type = 1
    elif user_choice == 'DOUBLE':
        cypher_type = 2
    elif user_choice == 'TRIPLE':
        cypher_type = 3
    today = datetime.today()
    cypher_file_name = today.strftime("%Y-%m-%d %H%M%S")
    cypher_list = []
    inc = 0
    if cypher_type == 1:
        cypher_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        random.shuffle(cypher_list)
    elif cypher_type == 2:
        cypher_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        cypher_list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        random.shuffle(cypher_list1)
        random.shuffle(cypher_list2)
        while inc <= 67:
            cypher_list_var = cypher_list1[inc] + cypher_list2[inc]
            cypher_list.append(cypher_list_var)
            inc += 1
    elif cypher_type == 3:
        cypher_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        cypher_list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        cypher_list3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
        random.shuffle(cypher_list1)
        random.shuffle(cypher_list2)
        random.shuffle(cypher_list3)
        while inc <= 67:
            cypher_list_var = cypher_list1[inc] + cypher_list2[inc] + cypher_list3[inc]
            cypher_list.append(cypher_list_var)
            inc += 1
    cypher_str = ''
    for item in cypher_list:
        if item == cypher_list[-1]:
            cypher_str = cypher_str + item
        else:
            cypher_str = cypher_str + item + '|'
    cypherhand = open(cypher_file_name + '_cypher.txt', "w")
    if cypher_type == 1:
        cypherhand.write('SINGLE\n' + cypher_str)
    elif cypher_type == 2:
        cypherhand.write('DOUBLE\n' + cypher_str)
    elif cypher_type == 3:
        cypherhand.write('TRIPLE\n' + cypher_str)
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
    cypher_list = cypher.split('|')
    cypherhand.close()
    cypher_message = input('What would you like to call the file containing the encoded message?\n')
    cmhand = open(cypher_message + ".txt", "w")
    chars_ordered_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    message_text = message_text_input.splitlines()
    today = datetime.today()
    today_str = today.strftime("%Y-%m-%d %H%M%S")
    today_str_enc = ''
    for char in today_str:
        if char in chars_ordered_lis:
            pos = chars_ordered_lis.index(char)
            today_char = char.replace(chars_ordered_lis[pos], cypher_list[pos])
            today_str_enc += today_char
    cypher_text_list = []
    for line in message_text:
        cypher_line = ''
        for char in line:
            if char in chars_ordered_lis:
                pos = chars_ordered_lis.index(char)
                cypher_char = char.replace(chars_ordered_lis[pos], cypher_list[pos])
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
    cypher_list = cypher.split('|')
    cypher_text_list = []
    chars_ordered_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    today = datetime.today()
    today_str = today.strftime("%Y-%m-%d %H%M%S")
    today_str_enc = ''
    for char in today_str:
        if char in chars_ordered_lis:
            pos = chars_ordered_lis.index(char)
            today_char = char.replace(chars_ordered_lis[pos], cypher_list[pos])
            today_str_enc += today_char
    for line in message_text:
        if line.startswith('*'):
            cypher_text_list.append(line)
        else:
            cypher_line = ''
            for char in line:
                if char in chars_ordered_lis:
                    pos = chars_ordered_lis.index(char)
                    cypher_char = char.replace(chars_ordered_lis[pos], cypher_list[pos])
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
    chars_ordered_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    message_hand = open(message_file_name + '.txt', 'r')
    cypher_string = message_hand.read()
    message_hand.close()
    cypher_text = cypher_string.splitlines()
    cypher_input = input('Please enter the filename of the cypher you would like to decrypt the message.\n')
    cypherhand = open(cypher_input + ".txt", "r")
    cypher = cypherhand.read()
    cypher_hand_list = cypher.splitlines()
    cypher_header = cypher_hand_list[0]
    cypher_body = cypher_hand_list[1]
    cypher_list = cypher_body.split('|')
    cypherhand.close()
    star_text_list = []
    encoded_text_list = []
    plain_text_list = []
    section_break = '*\n*------------------------------------------------\n*\n'
    for line in cypher_text:
        if line.startswith('*'):
            star_text_list.append(line)
        elif cypher_header == 'SINGLE':
            plain_line = ''
            for char in line:
                if char in cypher_list:
                    pos = cypher_list.index(char)
                    plain_char = char.replace(cypher_list[pos], chars_ordered_lis[pos])
                    plain_line += plain_char
            plain_text_list.append(plain_line)
            encoded_text_list.append('* ' + line)
        elif cypher_header == 'DOUBLE':
            inc = 0
            plain_line = ''
            cypher_double = ''
            while inc < len(line):
                cypher_double = line[inc:inc + 2]
                pos = cypher_list.index(cypher_double)
                plain_char = cypher_double.replace(cypher_list[pos], chars_ordered_lis[pos])
                plain_line += plain_char
                inc += 2
            plain_text_list.append(plain_line)
            encoded_text_list.append('* ' + line)
        elif cypher_header == 'TRIPLE':
            inc = 0
            plain_line = ''
            cypher_triple = ''
            while inc < len(line):
                cypher_triple = line[inc:inc + 3]
                pos = cypher_list.index(cypher_triple)
                plain_char = cypher_triple.replace(cypher_list[pos], chars_ordered_lis[pos])
                plain_line += plain_char
                inc += 3
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

#TODO: Create function that can strip off asterisks programatically for easier decryption
def decrypt_archive():
    print('''Let's decode an entire message history
    *Note: for proper file handling, it is recommended you make a copy of the encrypted message archive to decrypt and then delete it afterwards
    You will (1) provide the name of the file to decrypt and
    (2) provide the filename of the cypher used to encrypt it,
    in that order. The decoded message will appear after the encoded message''')

    chars_ordered_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    
    message_file_name = input('What is the name of the file? (Must be ".txt")\n')    
    message_hand = open(message_file_name + '.txt', 'r')
    cypher_string = message_hand.read()
    message_hand.close()
    cypher_text = cypher_string.splitlines()

    cypher_input = input('Please enter the filename of the cypher you would like to decrypt the message.\n')
    cypherhand = open(cypher_input + ".txt", "r")
    cypher = cypherhand.read()
    cypher_hand_list = cypher.splitlines()
    cypher_header = cypher_hand_list[0]
    cypher_body = cypher_hand_list[1]
    cypher_list = cypher_body.split('|')
    cypherhand.close()

    archive_list = []
    for line in cypher_text:
        if line == '*':
            archive_list.append('')
        elif line == '*------------------------------------------------':
            archive_list.append('------------------------------------------------')
        elif line.startswith('*'):
            archive_list.append(line[2:])
        else:
            archive_list.append(line)
    
    print(archive_list)
    plain_text_list = []
    for line in archive_list:
        if line == '------------------------------------------------':
            plain_text_list.append('------------------------------------------------')
        elif line == '':
            plain_text_list.append('')
        else:
            if cypher_header == 'SINGLE':
                plain_line = ''
                for char in line:
                    if char in cypher_list:
                        pos = cypher_list.index(char)
                        plain_char = char.replace(archive_list[pos], chars_ordered_lis[pos])
                        plain_line += plain_char
                plain_text_list.append(plain_line)
            elif cypher_header == 'DOUBLE':
                inc = 0
                plain_line = ''
                cypher_double = ''
                while inc < len(line):
                    cypher_double = line[inc:inc + 2]
                    pos = cypher_list.index(cypher_double)
                    plain_char = cypher_double.replace(cypher_list[pos], chars_ordered_lis[pos])
                    plain_line += plain_char
                    inc += 2
                plain_text_list.append(plain_line)
            elif cypher_header == 'TRIPLE':
                inc = 0
                plain_line = ''
                cypher_triple = ''
                while inc < len(line):
                    cypher_triple = line[inc:inc + 3]
                    pos = cypher_list.index(cypher_triple)
                    plain_char = cypher_triple.replace(cypher_list[pos], chars_ordered_lis[pos])
                    plain_line += plain_char
                    inc += 3
                plain_text_list.append(plain_line)
    plain_text_str = ''
    for line in plain_text_list:
        if line == '':
            plain_text_str = plain_text_str + '\n'
        elif line == plain_text_list[-1]:
            plain_text_str = plain_text_str + line
        else:
            plain_text_str = plain_text_str + line + '\n'
    message_hand = open(message_file_name + '.txt', 'w')
    message_hand.write(plain_text_str)
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
    5. Decode an entire message history as long as you have the correspond cypher
        To decode an entire message history enter the command: 'ARCHIVE'
    
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
    5. Decode an entire message history as long as you have the correspond cypher
        To decode an entire message history enter the command: 'ARCHIVE'
    
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
    elif user_choice == 'ARCHIVE':
        decrypt_archive()
    elif user_choice == 'HELP':
        help()
    elif user_choice == 'EXIT':
        print('\nGO FORTH SPYMASTER!\n')
    else:
        print("I don't understand your COMMAND, please try again\n")

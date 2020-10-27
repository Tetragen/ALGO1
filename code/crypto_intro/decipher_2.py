"""
break the second ciphering solution
"""

from random import randrange
from termcolor import colored

max_number_of_attempts = 10000


def decipher_2(text, key_size, extract):
    """
        from the coded message, find the original one based on an extract
        Again, we assume that we know that the word "COURSE" is in the original
        message.
    """
    print(f"code to decipher : {code}")
    attempt = 0
    decoded_message = ""
    while extract not in decoded_message and attempt < max_number_of_attempts:
        # try again
        decoded_message = ""
        # try a new key
        attempt += 1
        """
            EDIT HERE
        """
        key = [1]*key_size
        subkey = 0
        for character in text:
            ascii_index = ord(character)
            if ascii_index > 64 and ascii_index < 91:
                """
                    EDIT HERE
                """
                decoded_message += chr((key[subkey]) % 26 + 65)
                subkey = (subkey) % key_size
            else:
                decoded_message += character
        print(f"---\nattempt : {attempt}")
        print(f"key : {key}")
        print(colored(decoded_message, "green", attrs=["bold"]))
    if extract in decoded_message:
        print(f"success : key={key}")
    return decoded_message


with open("crypted_messages/crypted_message_2.txt", 'r') as text_file:
    code = text_file.read()

decipher_2(code, 3, "COURSE")

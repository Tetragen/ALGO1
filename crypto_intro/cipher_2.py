"""
second crypting method
"""

from random import randrange


def cipher_2(message, key_size):
    """
    the key size is a parameter of this method.
    How many subkeys do we want to use ?
    """
    key = [randrange(1, 27) for i in range(key_size)]
    print('key : ' + str(key))
    crypted_message = ""
    subkey = 0
    for character in message:
        # convert to ascii unicode code point
        ascii_index = ord(character)
        if ascii_index > 64 and ascii_index < 91:
            # change the unicode code point
            new_index = (ascii_index - 65 + key[subkey]) % 26 + 65
            # convert back to string
            crypted_message += chr(new_index)
            # change the subkey
            subkey = (subkey + 1) % key_size
        else:
            crypted_message += character
    with open("crypted_messages/crypted_message_2.txt", "w") as text_file:
        text_file.write(crypted_message)
    return crypted_message


print(cipher_2("ALGORITHM COURSE", 3))

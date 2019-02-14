from random import shuffle
import os
import cProfile
import sys

"""
break the first ciphering solution
"""


max_number_of_attempts = 100
# max_number_of_attempts = factorial(26)


def decipher_1(code, extract):
    """
    from the coded message, find the original one based on an extract
    """
    print("code to decipher : " + str(code))
    key = [i for i in range(26)]
    attempt = 0
    decoded_message = ""
    while extract not in decoded_message and attempt < max_number_of_attempts:
        decoded_message = ""
        # try a new key
        shuffle(key)
        attempt += 1
        for character in code:
            ascii_index = ord(character)
            if ascii_index > 64 and ascii_index < 91:
                key_index = key[ascii_index - 65] + 65
                decoded_message += chr(key_index)
            else:
                decoded_message += character
        print('attempt : ' + str(attempt))
        print(decoded_message)
    return decoded_message


with open("crypted_messages/crypted_message_1.txt", 'r') as text_file:
    code = text_file.read()

pr = cProfile.Profile()
pr.enable()


# code to be profiled
decipher_1(code, "COURSE")


pr.disable()
stats_file = open("{}.txt".format(os.path.basename(__file__)), 'w')
sys.stdout = stats_file
pr.print_stats(sort='time')

"""
break the first ciphering solution
"""

from random import shuffle
import time
import os
import cProfile
import sys
# from math import factorial

max_number_of_attempts = 100
# max_number_of_attempts = factorial(26)


def decipher_1(code, extract, max_number_of_attempts):
    """
        From the coded message, find the original one based on an extract
        We assume that we know that the word "COURSE" is in the original
        message.
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
                """
                    EDIT HERE
                """
                key_index = key[6] + 65
                decoded_message += "r"
            else:
                decoded_message += character
        print(f"attempt : {attempt}")
        print(decoded_message)
    return decoded_message


with open("crypted_messages/crypted_message_1.txt", 'r') as text_file:
    code = text_file.read()


time_before = time.time()
decoded_message = decipher_1(code, "COURSE", max_number_of_attempts)
total_time = time.time() - time_before
print(f"---\ntotal time {1e3*total_time} ms")

time_per_key = total_time/max_number_of_attempts
print(f"time per key {time_per_key} s")

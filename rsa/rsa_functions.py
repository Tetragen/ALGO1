"""
RSA : Rivest, Shamir, Adleman (1977)
"""

import math
from random import randrange
from itertools import count, islice


def generate_rsa_keys(p, q):
    """
                    Using two primary numbers p and q, generate the keys
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    # find a such that a and phi are coprime
    a = randrange(1, phi)
    while not math.gcd(a, phi) == 1:
        a += 1 % phi
    # find b such that ab=1[phi]
    # b is the inverse of a modulo phi
    r, b, v, r2, b2, v2 = a, 1, 0, phi, 0, 1
    # extended euclid algorithm
    while not (r2 == 0):
        q = r // r2
        r, b, v, r2, b2, v2 = r2, b2, v2, r - q * r2, b - q * b2, v - q * v2
    while b < 0:
        b += phi
    return(a, b)


def cipher_rsa(text, public_key):
    """
                    cipher a text with RSA algorithm
    """
    n = public_key[0]
    a = public_key[1]
    code = ''
    for character in text:
        ascii_index = ord(character)
        coded_index = ascii_index**a % n
        print(character + ' (' + str(ascii_index) + ')' +
              ' becomes ' + str(coded_index))
        code += str(coded_index) + ','
    # remove the last comma
    code = code[:-1]
    return(code)


def decipher_rsa(code, public_key, private_key):
    """
                    decipher the code
    """
    n = public_key[0]
    b = private_key
    # separate the commas
    code_str = code.split(',')
    # convert to integers
    # print(code_str)
    code_list = [int(x) for x in code_str]
    decoded_text = ''
    for coded_index in code_list:
        decoded_index = coded_index**b % n
        decoded_letter = chr(decoded_index)
        print(str(coded_index) + ' becomes ' + decoded_letter)
        decoded_text += decoded_letter
    return(decoded_text)


def find_private_key(public_key):
    """
            find the private key as a function
            of the public key n,a to break the RSA
    """
    n = public_key[0]
    a = public_key[1]
    # crucial step : find if n is a product of primary numbers
    p, q = primary_decomposition(n)
    # if yes, continue
    if not p == 0:
        # find b as before
        phi = (p - 1) * (q - 1)
        # b is the inverse of a modulo phi
        # extended euclid algorithm (as before)
        r, b, v, r2, b2, v2 = a, 1, 0, phi, 0, 1
        while not (r2 == 0):
            q1 = r // r2
            r, b, v, r2, b2, v2 = r2, b2, v2, r - q1 * r2, b - q1 * b2, v - q1 * v2
        while b < 0:
            b += phi
        return b, phi, p, q
    else:
        print('no primary decomposition found for n')
        # retur for convenience
        return 0, 0, 0, 0


def primary_decomposition(n):
    # there is no need for testing all the values below n
    # (see course)
    # print('searching primary decomposition of ' + str(n))
    for p_test in range(2, int(math.sqrt(n) + 1)):
        # check the remainder of
        # n/p_test to see if p_test divides n
        r_test = n % p_test
        if r_test == 0:
            # check if p_test is a primary number
            if isPrime(p_test):
                # print(str(p_test) + ' divides ' + str(n) + ' and is prime')
                q_test = n // p_test
                # check if q_test is a primary number
                if isPrime(q_test):
                    print('decomposition in prime factors of ' +
                          str(n) + ' : ' + str(p_test) + ',' + str(q_test))
                    return p_test, q_test
    print('no decomposition in primary numbers found')
    # return 0 for convenience
    return 0, 0


def isPrime(n):
    if n < 2:
        return False

    # we use a genertor to save memory
    for number in islice(count(2), int(math.sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

"""
double check if deciphering works not for students
"""

import rsa_functions


def decipher_hidden():
    for index in range(1, 5):
        # load the code
        with open('crypted_messages/crypted_message_rsa_' +
                  str(index) + '.txt', 'r') as code_txt:
            code = code_txt.read()

        print('code : ' + code)
        # load the keys
        with open('rsa_keys/public_key_' +
                  str(index) + '.txt', 'r') as text_file:
            public_key_str = text_file.read()

        with open('rsa_keys/private_key_' +
                  str(index) + '.txt', 'r') as text_file:
            private_key_str = text_file.read()

        # convert to integers
        n = int(public_key_str.split(',')[0])
        a = int(public_key_str.split(',')[1])
        b = int(private_key_str)

        public_key = (n, a)
        private_key = b
        print('public key : ' + str(public_key))
        print('private_key : ' + str(private_key))

        deciphered_text = rsa_functions.decipher_rsa(code,
                                                     public_key,
                                                     private_key)
        with open('decrypted_messages/decrypted_message_rsa_' +
                  str(index) + '.txt', "w") as text_file:
            text_file.write(deciphered_text)
        print("deciphered text : " + deciphered_text)


decipher_hidden()

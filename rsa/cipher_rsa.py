import rsa_functions

p, q = 17, 11
n = p * q
phi = (p - 1) * (q - 1)

a, b = rsa_functions.generate_rsa_keys(p, q)

public_key = (n, a)
private_key = b
print('public key : ' + str(public_key))
print('private_key : ' + str(private_key))

remainder = a * b % phi
if remainder == 1:
    print('keys are ok : b is the inverse of a modulo phi')
else:
    print('probem with keys ! b is not the inverse of a modulo phi')

# save the keys
with open("rsa_keys/generated_public_key.txt", 'w') as text_file:
    text = text_file.write(str(public_key[0]) + ',' + str(public_key[1]))

with open("rsa_keys/generated_private_key.txt", 'w') as text_file:
    text = text_file.write(str(b))

# text to code
with open("texts/example_text.txt", 'r') as text_file:
    text = text_file.read()

code = rsa_functions.cipher_rsa(text, public_key)

# save the code
with open("crypted_messages/crypted_message_rsa.txt", "w") as text_file:
    text_file.write(code)
print('code : ' + str(code))

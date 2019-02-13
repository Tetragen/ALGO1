import rsa_functions

index = 3

# load the public key
with open('rsa_keys/public_key_' + str(index) + '.txt', 'r') as text_file:
    public_key_str = text_file.read()


# convert to integers
n = int(public_key_str.split(',')[0])
a = int(public_key_str.split(',')[1])
public_key = (n, a)
print('public key file : public_key_' + str(index) + '.txt')
print('public key : ' + str(public_key))

private_key, phi, p, q = rsa_functions.find_private_key(public_key)
if not p == 0	:
    print('found private key : ' + str(private_key))
    print('p : ' + str(p))
    print('q : ' + str(q))
    print('phi : ' + str(phi))
else:
    print('did not find primary decomposition')


with open('crypted_messages/crypted_message_rsa_' +
          str(index) + '.txt', 'r') as code_txt:
    code = code_txt.read()

print('code : ' + code)

decoded_text = rsa_functions.decipher_rsa(code, public_key, private_key)
print('decoded text : ' + decoded_text)

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import errno

message = b'This is a message from me!'

try:
    with open('privkey.pem', 'r') as f:  # THis pem extension stores encrypted data
        key = RSA.import_key(f.read())

except IOError as e:
    if e.errno != errno.ENOENT:  # this enoent checks for files in directories
        raise  # and this if checks if error is about missing files

    # no private key, generate one
    key = RSA.generate(4096)
    with open('privkey.pem', 'wb') as f:
        f.write(key.export_key('PEM'))  # format in which we want to export the key

    with open('pubkey.pem', 'wb') as f:
        f.write(key.publickey().export_key('PEM'))  # key.publickey() will get key from rsa algoithm
        # and export that public key to this file pubkey.pem

hasher = SHA256.new(message)  # creates new hash object for our message and converts it to hash value
signer = PKCS1_v1_5.new(key)  # This creates or instantiates a signer object for holding private key

signature = signer.sign(hasher)  # It will be combination of ciphertext as it signs key on hash object

# print(signature)
with open('pubkey.pem', 'rb') as f:
    key = RSA.import_key(f.read())

hasher = SHA256.new(message)
verifier = PKCS1_v1_5.new(key)  # Instantiates a new verifier object

if verifier.verify(hasher, signature):
    print("Nice the signature is valid")

else:
    print("No, message is signed by wrong private key or its corrupted")

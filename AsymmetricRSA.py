from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Encrpytion done by sender
message = b'This is a secret message'

with open('pubkey.pem', 'rb') as f:
    key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(key)  # it instantiates a cipher object
encrypted = cipher.encrypt(message)
print(encrypted)

# Decryption done by receiver
with open('privkey.pem', 'rb') as f:
    key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(key)
decrypted = cipher.decrypt(encrypted)
print(decrypted)
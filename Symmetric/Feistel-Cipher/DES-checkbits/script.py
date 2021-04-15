from itertools import product

from Crypto.Cipher import DES

key = string.digits
key = [key[i] for i in range(0, len(key), 2)]
# print(list(map(ord, list(key))))

for iter_key in product(key, repeat=8):
    des = DES.new(''.join(iter_key), DES.MODE_ECB)
    ciphertext = bytes.fromhex(message_hex)
    plaintext = des.decrypt(ciphertext)
    if plaintext.decode() == message:
        print(DES.new(''.join(iter_key), DES.MODE_ECB).decrypt(bytes.fromhex(flag)))
        break



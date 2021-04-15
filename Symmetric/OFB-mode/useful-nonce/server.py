import os
import sys
from secret import FLAG
from Crypto.Cipher import AES

def pad(text):
    padding = 16 - (len(text) % 16)
    return text + bytes([padding] * padding)

def encrypt(text):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.encrypt(pad(text))

def nonce():
    randtext = list(os.urandom(len(FLAG.encode())))
    randtext = list(map(lambda x: (x + 0x7F) % 0xFF, randtext))
    randtext = bytes(randtext)
    return encrypt(randtext).hex()

if __name__ == '__main__':
    iv = os.urandom(16)
    key = os.urandom(32)
    print(f'flag: {encrypt(FLAG.encode()).hex()}')
    while True:
        print('> nonce')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'nonce':
            print(nonce())
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(encrypt(b'Bad hacker').hex())

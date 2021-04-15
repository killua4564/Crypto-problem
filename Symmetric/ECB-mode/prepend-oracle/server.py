import os
import sys
from secret import FLAG
from Crypto.Cipher import AES


def pad(text):
    padding = 16 - (len(text) % 16)
    return text + bytes([padding]) * padding

def unpad(text):
    padding = text[-1]
    assert 1 <= padding <= 16
    assert text.endswith(bytes([padding]) * padding)
    return text[:-padding]

def encrypt(text):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(text))

def enc():
    pretext = input('> Input pretext: ')
    print(pretext + FLAG, file=sys.stderr)
    print(encrypt((pretext + FLAG).encode()).hex(), file=sys.stderr)
    return encrypt((pretext + FLAG).encode()).hex()

if __name__ == '__main__':
    key = os.urandom(32)
    while True:
        print('> enc')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit': 
            sys.exit(1)
        elif cmd == 'enc':
            print(enc())
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(AES.new(key, AES.MODE_ECB).encrypt(pad(b'Bad hacker')).hex())

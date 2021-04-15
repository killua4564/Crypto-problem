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
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(pad(text))
    return enc

def decrypt(text):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        text = unpad(cipher.decrypt(text))
        return text
    except AssertionError:
        return b'Error'

def token():
    text = b'test123_guest'
    print(f'Token: {encrypt(text).hex()}')

def verify():
    text = decrypt(bytes.fromhex(input('> token: ')))
    if b'test123_guest' in text:
        print('Hi guest!')
        sys.exit(1)
    if b'user456_admin' in text:
        print('Hi admin!')
        print(f'Here is your flag: {FLAG}')
        print('[FLAG] padding-oracle', file=sys.stderr)
        sys.exit(1)
    if b'Error' in text:
        print('Error QQ')
    else:
        print('Bad hacker')

if __name__ == '__main__':
    iv = os.urandom(16)
    key = os.urandom(32)
    for _ in range(2048):
        print('> token')
        print('> verify')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit': 
            sys.exit(1)
        elif cmd == 'token':
            token()
        elif cmd == 'verify':
            verify()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(AES.new(key, AES.MODE_CBC, iv).encrypt(pad(b'Bad hacker')).hex())
    sys.exit(1)

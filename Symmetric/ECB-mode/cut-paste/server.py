import os
import sys
from urllib.parse import parse_qs, urlencode

from Crypto.Cipher import AES
from secret import FLAG


def pad(text):
    padding = 16 - (len(text) % 16)
    return text + bytes([padding] * padding)

def unpad(text):
    padding = text[-1]
    for char in text[-padding:]:
        assert char == padding
    return text[:-padding]

def register():
    user = input('> Username: ')
    token = urlencode({'user': user, 'admin': 'N'})
    token = cipher.encrypt(pad(token.encode())).hex()
    print(f'> Token: {token}\n')

def login():
    token = input('> Token: ')
    token = cipher.decrypt(bytes.fromhex(token))
    token = parse_qs(unpad(token).decode())
    for k, val in token.items():
        assert len(val) == 1
        if k == 'admin' and val[0] == 'Y':
            print(f'Here is your flag: {FLAG}')
            print('[FLAG] cut-paste', file=sys.stderr)
    print('> login finish, bye~')
    sys.exit(1)

if __name__ == '__main__':
    key = os.urandom(32)
    cipher = AES.new(key, AES.MODE_ECB)
    while True:
        print('> register')
        print('> login')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'register':
            register()
        elif cmd == 'login':
            login()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(cipher.encrypt(pad(b'Bad hacker')).hex())

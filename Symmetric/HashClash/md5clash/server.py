import os
import sys
from hashlib import md5

from secret import FLAG
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long

REGISTERED = set()
PREFIX = b'NTUSTISC'

def encrypt(text):
    ctr = Counter.new(128, initial_value=bytes_to_long(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.encrypt(text)

def decrypt(text):
    ctr = Counter.new(128, initial_value=bytes_to_long(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(text)

def register():
    global REGISTERED
    assert len(REGISTERED) < 3
    user = bytes.fromhex(input('> username: '))
    mac = md5(PREFIX + user + key).digest()
    token = encrypt(user + mac).hex()
    REGISTERED.add(user)
    print(f'Token: {token}')

def login():
    token = decrypt(bytes.fromhex(input('> token: ')))
    user, mac = token[:-16], token[-16:]
    if mac == md5(PREFIX + user + key).digest():
        if user not in REGISTERED:
            print(f'Cool, Here is your flag: {FLAG}')
            print('[FLAG] md5clash', file=sys.stderr)
            return
        print(f'Hi {user.hex()}!')
        return
    print('Invalid mac')

if __name__ == '__main__':
    iv = os.urandom(16)
    key = os.urandom(32)
    while True:
        print('> login')
        print('> register')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'login':
            login()
            sys.exit(1)
        elif cmd == 'register':
            register()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')

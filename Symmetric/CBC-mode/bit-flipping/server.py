import os
import sys
import msgpack  # pip install msgpack==0.6.0
from secret import FLAG
from Crypto.Cipher import AES


def pad(text):
    padding = (16 - (len(text) % 16)) % 16
    return text + bytes([padding] * padding)

def unpad(text):
    padding = text[-1]
    if padding < 16:
        assert text.endswith(bytes([padding] * padding))
        return text[:-padding]
    return text

def encrypt(text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(pad(text))
    return enc

def decrypt(text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(text)
    return unpad(dec)

def login():
    usr = input('> username: ')
    pwd = input('> password: ')
    vc = os.urandom(20).hex()
    token = {'usr': usr, 'pwd': pwd, 'vc': vc}
    token = msgpack.dumps(token)
    token = encrypt(token).hex()
    print(f'Token: {token}')

def verify():
    token = input('> token: ')
    vc = input('> verification code: ').encode()
    token = decrypt(bytes.fromhex(token))
    token = msgpack.loads(token)
    if vc != token.get(b'vc'):
        print('No hacking')
    else:
        print(f'Welcome {token.get(b"usr")}')
        print(f'Here is your flag: {FLAG}')
        print('[FLAG] bit-flipping', file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    iv = os.urandom(16)
    key = os.urandom(32)
    while True:
        print('> login')
        print('> verify')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit': 
            sys.exit(1)
        elif cmd == 'login':
            login()
        elif cmd == 'verify':
            verify()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(AES.new(key, AES.MODE_CBC, iv).encrypt(pad(b'Bad hacker')).hex())

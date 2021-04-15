import os
import sys
from secret import FLAG
from Crypto.Cipher import AES

def pad(text):
    padding = 16 - (len(text) % 16)
    return text + bytes([padding] * padding)

def CBC_MAC(text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    rawmac = cipher.encrypt(pad(text))[-16:]
    cipher = AES.new(key, AES.MODE_ECB)
    mac = cipher.encrypt(rawmac).hex().zfill(32)
    return mac

def challenge():
    m1 = input('> First (hex): ')
    m2 = input('> Second (hex): ')
    mac1, mac2 = CBC_MAC(bytes.fromhex(m1)), CBC_MAC(bytes.fromhex(m2))
    if mac1 == mac2:
        if m1 == m2:
            print('You must not hacker owo.')
            return
        print(f'Here is your flag: {FLAG}')
        print('[FLAG] CBC-MAC', file=sys.stderr)
        sys.exit(1)
    else:
        print(f'Try hard!! {mac1} != {mac2}')

if __name__ == '__main__':
    print('Give me 2 plaintext with same MAC.')
    iv = os.urandom(16)
    key = os.urandom(32)
    while True:
        print('> challenge')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'challenge':
            challenge()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(AES.new(key, AES.MODE_ECB).encrypt(pad(b'Bad hacker')).hex())
            
import os
import sys
from secret import FLAG
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long

def pad(text):
    padding = (16 - (len(text) % 16)) % 16
    return text + bytes([padding] * padding)

def unpad(text):
    padding = text[-1]
    if padding < 16:
        assert text.endswith(bytes([padding]) * padding)
        return text[:-padding]
    return text

def encrypt(text):
    global iv
    iv = os.urandom(1)
    ctr = Counter.new(128, initial_value=bytes_to_long(iv))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(pad(text))

def decrypt(text):
    ctr = Counter.new(128, initial_value=bytes_to_long(iv))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return unpad(cipher.decrypt(text))

def flag():
    text = bytes.fromhex(input('> flag: '))
    if FLAG == decrypt(text).decode():
        print(f'This is FLAG: {encrypt(FLAG.encode()).hex()}')
    else:
        print('This is not FLAG')

if __name__ == '__main__':
    iv = os.urandom(16)
    key = os.urandom(32)
    print(f'Initialize flag: {encrypt(FLAG.encode()).hex()}')
    while True:
        print('> flag')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit()
        elif cmd == 'flag':
            flag()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print(encrypt(b'Bad hacker').hex())

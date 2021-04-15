import sys
from random import randint

from Crypto.Cipher import DES
from secret import FLAG

hello_text = b'Hello, World!!! By: DES!'

flag = lambda: cipher.encrypt(FLAG).hex()
hello = lambda: cipher.encrypt(hello_text).hex()

def init():
    key = str(randint(0, 99999999)).zfill(8).encode()
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher

if __name__ == '__main__':
    cipher = init()
    while True:
        print('1) Say Hello to DES')
        print('2) Get encrypted flag')
        print('3) print server code')
        print('0) exit')
        n = input('Enter: ').strip('\n').strip()
        if n == '0': 
            sys.exit(1)
        elif n == '1':
            print(hello())
        elif n == '2':
            print(flag())
        elif n == '3':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')
            
import os
import sys
from secret import FLAG
from Crypto.Cipher import AES

SECRET1 = os.urandom(16)
SECRET2 = os.urandom(16)
SECRET3 = os.urandom(16)
SECRET4 = os.urandom(16)

xor = lambda x, y: bytes([i ^ j for i, j in zip(x, y)])
block = lambda x: [x[i:i+16] for i in range(0, len(x), 16)]

def encrypt(text):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return iv + cipher.encrypt(text)

def decrypt(text):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.decrypt(text)

def secret():
    print('Which secret do you want?')
    print('> SECRET1')
    print('> SECRET2')
    print('> SECRET3')
    print('> SECRET4')
    secret_name = input('> input: ')
    if secret_name in ('SECRET1', 'SECRET2', 'SECRET3', 'SECRET4'):
        print(encrypt(globals().get(secret_name)).hex())
        return
    print('Bad hacker')

def challenge():
    plaintext = SECRET1 + SECRET2 + SECRET3 + SECRET4
    print(f'Problem: {encrypt(plaintext).hex()}')
    ciphertext = bytes.fromhex(input('> Answer: '))
    plaintext_block = block(decrypt(ciphertext))
    if SECRET3 == plaintext_block[2]:
        if SECRET2 == plaintext_block[3]:
            if SECRET1 in plaintext_block[4:]:
                padding = bytes.fromhex(input('> Great, chance to padding: '))
                if SECRET4 == xor(plaintext_block[1], padding):
                    print(f'Congratulations, Here is your flag: {FLAG}')
                    print('[FLAG] secret-game', file=sys.stderr)
                    return
                print(f'Wrong Answer, SECRET4 = {SECRET4.hex()}, BLOCK1 = {plaintext_block[1].hex()}')
                return
            print(f'Wrong Answer, SECRET1 = {SECRET1.hex()}, BLOCK4 = {b"".join(plaintext_block[4:]).hex()}')
            return
        print(f'Wrong Answer, SECRET2 = {SECRET2.hex()}, BLOCK3 = {plaintext_block[3].hex()}')
        return
    print(f'Wrong Answer, SECRET3 = {SECRET3.hex()}, BLOCK2 = {plaintext_block[2].hex()}')
    return

if __name__ == '__main__':
    iv = os.urandom(16)
    key = os.urandom(32)
    while True:
        print('> secret')
        print('> challenge')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit': 
            sys.exit()
        elif cmd == 'secret':
            secret()
        elif cmd == 'challenge':
            challenge()
            sys.exit(1)
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')

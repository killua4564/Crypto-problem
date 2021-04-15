import os
import sys
from Crypto.Cipher import AES
from secret import FLAG


iv = os.urandom(16)
key = os.urandom(32)
auth = os.urandom(16)

def encrypt():
    plaintext = input('Input a string to encrypt: ')
    if len(plaintext) < len(FLAG[0]):
        sys.exit(1)
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv).update(auth)
    print(f'ciphertext: {cipher.encrypt(plaintext.encode()).hex()}')
    print(f'tag: {cipher.digest().hex()}')

def decrypt():
    ciphertext = bytes.fromhex(input('ciphertext: '))
    tag = bytes.fromhex(input('tag: '))
    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv).update(auth)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode()
    except ValueError:
        print('Decryption failed :(')
        return
    if plaintext == FLAG[0]:
        print(f'Decrypt one flag and get one free, flag: {FLAG[1]}')
        print('[FLAG] forbidden-attack', file=sys.stderr)
    else:
        print(f'Here is your decrypted string: {plaintext}')

menu = {
    'encrypt': encrypt,
    'decrypt': decrypt,
    'server.py': lambda: print(open('./server.py', 'r').read()),
    'exit': lambda: sys.exit(1)
}

if __name__ == '__main__':
    print(f'flag: {AES.new(key, AES.MODE_GCM, nonce=iv).encrypt_and_digest(FLAG[0].encode())[0].hex()}')
    for _ in range(10):
        print('> encrypt')
        print('> decrypt')
        print('> server.py')
        print('> exit')
        choice = input('> Command: ')
        if not menu.get(choice):
            print('Not a valid choice...')
            sys.exit(1)
        menu.get(choice)()
    sys.exit(1)

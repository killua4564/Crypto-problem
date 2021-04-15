import os
import sys
from secret import FLAG

def KSA(key):
    S, j = list(range(256)), 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, size):
    i, j, key = 0, 0, []
    for _ in range(size):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key.append(S[(S[i] + S[j]) % 256])
    return bytes(key)

class RC4:

    def __init__(self, key, plaintext):
        self.S = KSA(list(key))
        self.key = PRGA(self.S, len(plaintext))
        self.plaintext = plaintext

    def cipher(self):
        ciphertext = []
        for i, j in zip(self.key, self.plaintext):
            ciphertext.append(i ^ j)
        return bytes(ciphertext)


if __name__ == '__main__':
    key = os.urandom(32)
    print(f'flag: {RC4(key, FLAG.encode()).cipher().hex()}')
    while True:
        print('> something')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'something':
            print(RC4(key, input('> say something: ').encode()).cipher().hex())
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')

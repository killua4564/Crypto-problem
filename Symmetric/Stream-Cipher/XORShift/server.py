import os
import sys
from secret import FLAG
from Crypto.Util.number import bytes_to_long

MASK = (1 << 64) - 1

def xorshift(nonce):
    nonce ^= (nonce & MASK) << 13
    nonce ^= (nonce & MASK) >> 7
    nonce ^= (nonce & MASK) << 17
    return nonce & MASK

def challenge():
    problem = ''
    nonce = bytes_to_long(os.urandom(8))
    for _ in range(200):
        nonce = xorshift(nonce)
        if bytes_to_long(os.urandom(1)) >= 128:
            problem += str(nonce & 1)
        else:
            problem += '.'

    print(f'Problem: {problem}')
    if nonce == int(input('Answer: ')):
        print(f'Yes, here is your flag: {FLAG}')
        print('[FLAG] XORShift', file=sys.stderr)
        return
    print('Wrong Answer.')
    return


if __name__ == '__main__':
    print('Welcome to XORShift server, guess random number.')
    while True:
        print('> challenge')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'challenge':
            challenge()
            sys.exit(1)
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')

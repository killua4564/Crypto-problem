import os
import sys

from Crypto.Cipher import AES
from Crypto.Random.random import randrange

from secret import FLAG

aes = AES.new(os.urandom(16), AES.MODE_ECB)
enc = lambda x: aes.encrypt(x.to_bytes(16, 'big')).hex()
dec = lambda x: int.from_bytes(aes.decrypt(bytes.fromhex(x)), 'big')

p = 0xfffffed83c17                    # |G| = P            # prime
ACTION = {
    'inv': lambda x: (-x) % p,        # (g^x)^-1  = g^(-x)
    'mul': lambda x, y: (x + y) % p,  # g^x * g^y = g^(x+y)
    'dhp': lambda x, y: x * y % p,    # enjoy your oracle!
}

def challenge():
    y = randrange(p)
    print(enc(1), enc(y))

    for _ in range(0x400):
        print('> inv x')
        print('> mul x y')
        print('> dhp x y')
        print('> sol y')

        action, *value = input('> Action: ').strip().split()
        if ACTION.get(action):
            print(enc(ACTION.get(action)(*map(dec, value))))

        if action == 'sol':
            if int(value[0]) == y:
                print(FLAG)
            return

if __name__ == '__main__':
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

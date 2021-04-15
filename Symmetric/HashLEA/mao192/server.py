import base64
import os
import sys

from hashlib import sha256
from math import cos

from secret import FLAG, SECRET_PASSWORD

username = b''
session = b''

USERS = {}
USERS[b'Admin'] = SECRET_PASSWORD
USERS[b'Guest'] = b'No FLAG'

def mao192(s):
    A = 0x41495333
    B = 0x7b754669
    C = 0x6e645468
    D = 0x65456173
    E = 0x74657245
    F = 0x6767217D

    G = lambda x, y, z: (x ^ (~z | ~y) ^ z) & 0xFFFFFFFF
    H = lambda x, y, z: (x ^ y ^ z & x) & 0xFFFFFFFF
    I = lambda x, y, z: ((x & ~z) | (~z & y)) & 0xFFFFFFFF
    J = lambda x, y, z: ((x ^ ~z) | (x & ~y)) & 0xFFFFFFFF
    K = lambda x, y, z: ((~x & z) | (~x & z ^ ~y)) & 0xFFFFFFFF
    L = lambda x, y, z: ((~x & y ^ z) | (x & y)) & 0xFFFFFFFF
    M = lambda x, y: (x << y | x >> (32 - y)) & 0xFFFFFFFF

    x = [int((0xFFFFFFFE) * cos(i)) & 0xFFFFFFFF for i in range(256)]
    s_size = len(s)
    s += bytes([0xb0])
    if len(s) % 128 > 120:
        while len(s) % 128 != 0:
            s += bytes(1)
    while len(s) % 128 < 120:
        s += bytes(1)
    s += bytes.fromhex(hex(s_size * 8)[2:].rjust(16, '0'))

    for i, b in enumerate(s):
        k, l = int(b), i & 0x1f
        A = (B + M(A + G(B,C,D) + x[k], l)) & 0xFFFFFFFF
        B = (C + M(B + H(C,D,E) + x[k], l)) & 0xFFFFFFFF
        C = (D + M(C + I(D,E,F) + x[k], l)) & 0xFFFFFFFF
        D = (E + M(D + J(E,F,A) + x[k], l)) & 0xFFFFFFFF
        E = (F + M(E + K(F,A,B) + x[k], l)) & 0xFFFFFFFF
        F = (A + M(F + L(A,B,C) + x[k], l)) & 0xFFFFFFFF
    return ''.join(map(lambda x : hex(x)[2:].zfill(8), [A, F, C, B, D, E]))

def verify(*stuff):
    return mao192(b'&&'.join(stuff)).encode()

def login():
    global username, session
    session = os.urandom(10).hex().encode()
    username = input('Please Input your username: ').encode()
    if b'&' in username:
        print('Bad hacker')
        sys.exit(1)
    password = USERS.get(username)
    if not password:
        print('Are you new here?')
        password = input('Let\'s set a password: ').encode()
        USERS[username] = password
        print('Well done.\n')
    print(f'Hello {username.decode()}')
    print(f'Here is your session ID: {session.decode()}')
    print(f'and your MAC(username&&password&&sessionID): {verify(username, password, session).decode()}')

def command():
    mac, *sess, cmd = base64.b64decode(input('What do you want to do?\n').encode()).split(b'&&')
    if mac == verify(username, USERS.get(username), *sess, cmd) and session in sess and session != b'':
        if cmd == b'flag':
            if username == b'Admin':
                print(f'Here is your flag: {FLAG}')
                print('[FLAG] mao192', file=sys.stderr)
                return
            print('Permission denial')
            return 
        print('Unknown command')
        return
    print('Refused')
    return

if __name__ == '__main__':
    print('Welcome to our system!')
    while True:
        print('> login')
        print('> command')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'login':
            login()
        elif cmd == 'command':
            command()
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')
    
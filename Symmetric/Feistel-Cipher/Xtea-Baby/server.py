import os
import struct
import sys
from secret import FLAG

def pad(text):
    padding = 16 - (len(text) % 16)
    return text + bytes([padding] * padding)

class Xtea:

    def __init__(self, key, rounds):
        assert len(key) == 16
        assert int(rounds) > 0

        self.key = struct.unpack('<4L', key)
        self.rounds = int(rounds)

    def encrypt(self, pt):
        ct = b''
        pt = pad(pt)
        for i in range(0, len(pt), 8):
            pt_block = bytes(pt[i:i+8])
            v0, v1 = struct.unpack('<2L', pt_block)
            sum, delta = 0, 0x9E3779B9
            for _ in range(self.rounds):
                v0 = (v0 + (((v1 << 4 ^ v1 >> 5) + v1) ^ (sum + self.key[sum & 3]))) & 0xFFFFFFFF
                sum = (sum + delta) & 0xFFFFFFFF
                v1 = (v1 + (((v0 << 4 ^ v0 >> 5) + v0) ^ (sum + self.key[sum >> 11 & 3]))) & 0xFFFFFFFF
            ct += struct.pack('<2L', v0, v1)
        return ct

if __name__ == '__main__':
    key = os.urandom(16)
    xtea = Xtea(key, 32)
    while True:
        print('> key')
        print('> flag')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit(1)
        elif cmd == 'key':
            print(key.hex())
        elif cmd == 'flag':
            print(xtea.encrypt(FLAG.encode()).hex())
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')

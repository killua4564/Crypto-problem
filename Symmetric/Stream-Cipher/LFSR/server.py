import sys
from secret import FLAG, REGISTER, TAPS

assert FLAG.startswith('flag')
assert len(REGISTER) == 16
assert len(TAPS) == 5

class LFSR:

    def __init__(self, register, taps):
        self.register = register
        self.taps = taps

    def next(self):
        new = 0
        ret = self.register[0]
        for i in self.taps:
            new ^= self.register[i]
        self.register = self.register[1:] + [new]
        return ret

def encrypt():
    enc_flag = []
    for char in FLAG.encode():
        enc_char = 0
        for binary in '{:08b}'.format(char):
            enc_char <<= 1
            enc_char += (int(binary) ^ lfsr.next())
        enc_flag.append(enc_char)
    return bytes(enc_flag)

if __name__ == '__main__':
    lfsr = LFSR(REGISTER, TAPS)

    while True:
        print('> flag')
        print('> server.py')
        print('> exit')
        cmd = input('> Command: ')
        if cmd == 'exit':
            sys.exit()
        elif cmd == 'flag':
            print(encrypt().hex())
        elif cmd == 'server.py':
            print(open('./server.py', 'r').read())
        else:
            print('Bad hacker')

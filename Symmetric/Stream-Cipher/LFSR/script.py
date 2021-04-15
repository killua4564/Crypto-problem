from itertools import combinations

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

register = list(map(int, ('{:08b}'.format(i ^ j) for i, j in zip(b'flag', flag_enc))))

print('register: ', register)
for i in combinations(list(range(16)), 5):
    lfsr = LFSR(register[:16], list(i))
    if all(bit == lfsr.next() for bit in register):
        taps = list(i)
        break

print('taps: ', taps)
lfsr = LFSR(register[:16], taps)

flag = []
for char in flag_enc:
    dec_char = 0
    for binary in '{:08b}'.format(char):
        dec_char <<= 1
        dec_char += int(binary) ^ lfsr.next()
    flag.append(dec_char)
print(bytes(flag).decode())

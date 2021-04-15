import struct

class Xtea:

    def __init__(self, key, rounds):
        assert len(key) == 16
        assert int(rounds) > 0

        j = 0
        self.S = list(range(256))
        self.key = struct.unpack('<4L', key)
        self.rounds = int(rounds)

        for i in range(256):
            j = (j + self.S[i] + key[i % 16]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def decrypt(self, ct):
        pt = b''
        for i in range(0, len(ct), 8):
            ct_block = bytes(ct[i:i+8])
            v0, v1 = struct.unpack('<2L', ct_block)
            sum, delta = (0x9E3779B9 * self.rounds) & 0xFFFFFFFF , 0x9E3779B9
            for _ in range(self.rounds):
                v1 = (v1 - (((v0 << 4 ^ v0 >> 5) + v0) ^ (sum + self.key[sum >> 11 & 3]))) & 0xFFFFFFFF
                sum = (sum - delta) & 0xFFFFFFFF
                v0 = (v0 - (((v1 << 4 ^ v1 >> 5) + v1) ^ (sum + self.key[sum & 3]))) & 0xFFFFFFFF
            pt += struct.pack('<2L', v0, v1)
        return unpad(pt)

if __name__ == '__main__':
    print(Xtea(key, 32).decrypt(flag).decode())
    
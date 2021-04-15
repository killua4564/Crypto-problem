from hashlib import sha512

from Crypto.Util.number import *
from Crypto.Random.random import randrange

from secret import FLAG

xor = lambda x, y: bytes(i ^ j for i, j in zip(x, y))

def genkey():
    g = 2
    while True:
        p = 2
        for _ in range(50):
            p *= getPrime(randrange(38, 42))
        if isPrime(p + 1):
            if pow(g, p // 2, p + 1) == p:
                return g, p + 1

if __name__ == '__main__':
    g, p = genkey()
    x = randrange(p - 1)
    h = pow(g, x, p)

    x = sha512(long_to_bytes(x)).digest()

    print(f'p = {p}')
    print(f'h = {h}')
    print(f'flag = {xor(FLAG.encode().ljust(len(x), bytes(1)), x).hex()}')

# p = 49030137971888168048837307477710599602566074389976901383856878142020689729786115229104108611435107
# h = 26510761486155174902684480389960593456643299898088422414230044409459111788468680630319305386383447
# flag = 979fa8a7f0b080178cf3d0fddba25ead51a1ebde430940f65b8e17e2db6f42bd1815c673f8d99cb9f78cef1f9bd237249b0a4d55169509a971fe85f14661d859

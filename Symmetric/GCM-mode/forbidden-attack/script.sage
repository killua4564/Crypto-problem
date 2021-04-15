
def bytes_to_poly(data, x):
    poly = 0
    data = '{:0128b}'.format(int.from_bytes(data, 'big'))
    for idx, bit in enumerate(data):
        poly += int(bit) * x ** idx
    return poly

def poly_to_hex(poly):
    data = 0
    for idx, bit in enumerate(poly._vector_()):
        data += int(bit) << (127 - idx)
    return hex(data)[2:]

def chuck(data, x):
    data += b'\x00' * (16 - (len(data) % 16))
    return list(bytes_to_poly(data[i:i+16], x) for i in range(0, len(data), 16))

pt1 = 'a' * 36
pt2 = 'b' * 36
ct1, t1 = encrypt(pt1)
ct2, t2 = encrypt(pt2)
print(f'flag[0] = {xor(pt1.encode(), ct1, flag).decode()}')

'''
t1 = A * H**5 + C11 * H**4 + C12 * H**3 + C13 * H**2 + L * H + E(J0)
t2 = A * H**5 + C21 * H**4 + C22 * H**3 + C23 * H**2 + L * H + E(J0)

t1 - t2 = (C11 - C21) * H**4 + (C12 - C22) * H**3 + (C13 - C23) * H**2
'''

F.<x> = GF(2**128)
P.<h> = PolynomialRing(F)

c11, c12, c13 = chuck(ct1, x)
c21, c22, c23 = chuck(ct2, x)
flag1, flag2, flag3 = chuck(flag, x)
t1, t2 = bytes_to_poly(t1, x), bytes_to_poly(t2, x)

f = (c11 - c21) * h ** 4 + (c12 - c22) * h ** 3 + (c13 - c23) * h ** 2 - (t1 - t2)
for root, _ in f.roots():
    tag = poly_to_hex(t1 + (flag1 - c11) * root ** 4 + (flag2 - c12) * root ** 3 + (flag3 - c13) * root ** 2)
    res = decrypt(flag.hex(), tag)
    if res:
        print(f'flag[1] = {res}')
        break

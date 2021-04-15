from Crypto.Util.number import *
from Crypto.Random.random import randrange
from gmpy2 import iroot

from secret import FLAG

def gen():
    p, q = 0, 1
    while abs(p - q) >= min(p, q):
        p, q = getPrime(1024), getPrime(1024)

    n = p * q
    phi = (p-1) * (q-1)

    e, d = 0, 0
    while GCD(e, phi) > 1 or d >= int(iroot(n, 4)[0]) // 3:
        d = getPrime(201)
        e = inverse(d, phi)

    return e, n

if __name__ == '__main__':
    m, (e, n) = bytes_to_long(FLAG.encode()), gen()
    print(f'(e, n) = {(e, n)}')
    print(f'flag = {pow(m, e, n)}')

# e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
# n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
# c = 84740524770381403153622925447792920959815469600692319965596776738431504244164788253920072346154965475345520986566261139605189850053220984036986688956922312943484012082747435674795128749623149324459566588589685250817942108728364336944750553593289462772627326115549452684668188298340307743571301091011089977112

'''
p % 4 = 3
m ** 2 % p = c

m ** (p-1) % p = 1
==> c ** (p-1)/2 % p = 1
==> c ** (p+1)/2 % p = c (p=4k+3)
==> c ** (4k+3+1)/2 % p = c
==> c ** (2k+2) % p = c
==> c ** (k+1) % p = m (k=(p-3)/4)
==> c ** (p-3)/4+1 % p = m
==> c ** (p+1)/4 % p = m
'''

def power2roots(a, k):
    def modular_sqrt(a, p): # Tonelli-Shanks algorithm (a < p)
        def legendre_symbol(a, p):
            ls = pow(a, (p - 1) // 2, p)
            return -1 if ls == p - 1 else ls

        if a == 1:
            return 1

        if a == 0 or p == 2 or legendre_symbol(a, p) != 1:
            return 0

        if p % 4 == 3:
            return pow(a, (p + 1) // 4, p)

        s, e = p - 1, 0
        while s % 2 == 0:                   # s * 2 ** e = p - 1
            s, e = s // 2, e + 1

        n = 2
        while legendre_symbol(n, p) != -1:  # n ** (p-1)/2 % p = p - 1
            n += 1

        x = pow(a, (s + 1) // 2, p)
        b = pow(a, s, p)
        g = pow(n, s, p)
        while True:
            t, m = b, 0
            for m in range(e):
                if t == 1:
                    break
                t = pow(t, 2, p)
            if m == 0:
                return x
            gs = pow(g, 2 ** (e - m - 1), p)
            g = (gs * gs) % p
            x = (x * gs) % p
            b = (b * g) % p
            e = m

    def chinese_remainder(n, a):
        sum = 0
        prod = functools.reduce(lambda a, b: a*b, n)
        for ni, ai in zip(n, a):
            p = prod // ni
            sum += ai * inverse(p, ni) * p
        return sum % prod

    if k == 0: 
        yield a
        return

    modular = (p, q1, q2)
    for item in power2roots(a, k-1):
        sroot = tuple(modular_sqrt(item, i) for i in modular)
        if sroot[0] and sroot[1] and sroot[2]:
            for iter in itertools.product((0, 1), repeat=3):
                iter = (abs(i - j * it) for i, j, it in zip(sroot, modular, iter))
                yield chinese_remainder((p, q1, q2), iter)

p = pollard(n)
q1, q2 = fermat_revise(n // p)

# power2roots(pow(flag, inverse(e, phi), n), int(math.log2(GCD(e, phi))))


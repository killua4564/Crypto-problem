
def baby_giant(g, h, n):
    # restore pow(g, k * sqrt(n), p)
    # match x with h * pow(g, x, p) % p
    # log(g, h, n) = (k * sqrt(n) - x) % n
    giant = {}
    sqrt = int(isqrt(n)) + 1
    gs, gks = pow(g, sqrt, p), 1
    for k in trange(sqrt, leave=False):
        giant[gks] = k
        gks = gks * gs % p

    for x in trange(sqrt, leave=False):
        if giant.get(h):
            k = giant.get(h)
            return (k * sqrt - x) % n
        h = h * g % p

ords = []
for i in tqdm(factor_list):
    gi = pow(g, (p - 1) // i, p)
    hi = pow(h, (p - 1) // i, p)
    ords.append(baby_giant(gi, hi, i))

x = chinese_remainder(factor_list, ords)
assert pow(g, x, p) == h

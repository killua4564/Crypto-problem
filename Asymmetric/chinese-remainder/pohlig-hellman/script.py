p = 0xfffffed83c17
factor_list = [(2, 1), (3, 2), (7, 1), (13, 4), (47, 1), (103, 1), (107, 1), (151, 1)]

def getmul(x, y):
    if x == one:
        return y
    if y == one:
        return x
    return mul(x, y)

def getexps(x):
    exps = [x]
    for _ in range(p.bit_length()):
        exps.append(getmul(exps[-1], exps[-1]))
    return exps

def exp(x, exps):
    res = tuple(item for item, bit in zip(exps, reversed('{:b}'.format(x))) if bit == '1')
    if len(res) == 0:
        return one
    return reduce(getmul, res)

def chinese_remainder(n, r):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for ni, ri in zip(n, r):
        Ni = prod // ni
        sum += ri * inverse(Ni, ni) * Ni
    return sum % prod

''' sage
IntegerModRing(0xfffffed83c17).multiplicative_generator()
>>> 5
'''

one, y = init()
two = add(one, one)
g = add(one, add(two, two))

gexps = getexps(g)
yexps = getexps(y)

gi = exp(phi-1, gexps)
giexps = getexps(gi)

# y = pow(g, x, p)
# find x then can compute y
gords = []
for fi, pi in factor_list:
    oi = 0
    gi = exp(phi // fi, gexps)
    for pj in range(1, pi+1):
        gt = one
        yj = getmul(exp(phi // (fi ** pj), yexps), exp(oi * phi // (fi ** pj), giexps))
        for oj in range(fi):
            if gt == yj:
                oi += oj * (fi ** (pj - 1))
                break
            gt = getmul(gt, gi)
    gords.append(oi)

x = chinese_remainder(list(map(lambda x: x[0] ** x[1], factor_list)), gords)
print(sol(pow(5, x, p)))


c2 = inverse(c2, n)
s1 = inverse(e1, e2)
s2 = (s1 * e1 - 1) // e2
flag = (pow(c1, s1, n) * pow(c2, s2, n)) % n

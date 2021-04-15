
N1 = n2 * n3
N2 = n1 * n3
N3 = n1 * n2

d1 = inverse(N1, n1)
d2 = inverse(N2, n2)
d3 = inverse(N3, n3)

flag = root((c1 * d1 * N1 + c2 * d2 * N2 + c3 * d3 * N3) % (n1 * n2 * n3), e)

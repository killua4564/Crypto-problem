
p = pollard(n)
q1, q2 = fermat(n // p)
d = inverse(e, (p-1) * (q1-1) * (q2-1))

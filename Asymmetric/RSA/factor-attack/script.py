
k = (key2[0] - key1[0] - 4) // 2
phi1 = key1[0] - k + 1
phi2 = key1[0] + k + 1

p3 = gmpy2.isqrt(key3[0])
phi3 = p3 * (p3 - 1)

flag = pow(flag, inverse(e, phi3), key3[0])
flag = pow(flag, inverse(e, phi2), key2[0])
flag = pow(flag, inverse(e, phi1), key1[0])

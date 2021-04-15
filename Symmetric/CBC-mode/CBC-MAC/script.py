
a = 'a' * 30
b = 'b' * 30
padding = '01' + '0' * 32

x, y = challenge(a, b)
challenge(a + padding + x, b + padding + y)

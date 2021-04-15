'''
user={name}&admin=N
user=(a * 11) | Y (O * 15)| (O * 16) | &admin=N ... (token1)
user=(a * 4)&admin= | N ... (token2)
'''

user1 = b'a' * 11 + b'Y' + b'O' * 31
user2 = b'a' * 4

token1 = block(register(user1))
token2 = block(register(user2))

payload = token2[0] + token1[1] + token1[2] * 4
login(payload)

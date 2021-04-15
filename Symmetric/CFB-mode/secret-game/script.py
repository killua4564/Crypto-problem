
P1P4 = xor(secret(1), secret(4))
P2P4 = xor(secret(2), secret(4))

conn.sendline('challenge')
C = block(bytes.fromhex(conn.recvuntil('\n').decode()))

payload = C[0] + C[2] + C[3] + xor(C[4], P2P4) + C[0] + C[1]
conn.sendline(payload.hex())

padding = xor(C[1], C[2], P1P4)
conn.sendline(padding.hex())

print(conn.recv())

'''
E(iv, key) xor P1 = C1
E(C1, key) xor P2 = C2
E(C2, key) xor P3 = C3
E(C3, key) xor P4 = C4

construct P = sth || P3 || P2 || ... || P1
sth part can use last padding chance to change

C = iv || C2 || C3 || C4 xor P2 xor P4 || iv || C1
D(C, key) = P1 xor C1 xor C2 || P3 || P2 || idk || P1
so, last padding must be P1 xor P4 xor C1 xor C2
'''

def nonce():
    conn.recvuntil(': ')
    conn.sendline('nonce')
    return bytes.fromhex(conn.recvuntil('\n').decode().strip('\n'))

arr = [nonce() for _ in range(4096)]

ff = b''
for idx in range(len(arr[0])):
    hs = set(list(range(256)))
    for item in arr:
        if item[idx] in hs:
            hs.remove(item[idx])
    if len(hs) == 1:
        ff += bytes(list(hs))
        continue

print(xor(flag, ff, b'\xff' * len(ff)))

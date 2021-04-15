
def pad(text):
    padding = (16 - (len(text) % 16)) % 16
    return text + bytes([padding] * padding)

def nonce():
    conn.recvuntil(': ')
    conn.sendline('nonce')
    return bytes.fromhex(conn.recvuntil('\n').decode().strip('\n'))

conn.recvuntil(': ')
flag = bytes.fromhex(conn.recvuntil('\n').decode().strip('\n'))

counter = [nonce() for _ in range(1024)]
pt = pad(b'Bad hacker')

for f in block(flag):
    for ctr in counter:
        flag_test = xor(f, pt, ctr)
        if all(char in string.printable.encode() for char in flag_test):
            print(flag_test)

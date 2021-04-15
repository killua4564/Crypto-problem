

def pad(text):
    padding = 16 - (len(text) % 16)
    return text + bytes([padding]) * padding

'''
D(token, key) = plaintext ^ iv
D(fake_iv || token, key) = idk || plaintext ^ iv ^ fake_iv

oracle padding to \x16 * 16
get origin iv by knowing plaintext and fake_iv
'''

fake_iv = b''
token = token()
for step in range(16):
    for char in range(256):
        test_iv = bytes(15 - step) + bytes([char]) + fake_iv
        if verify(test_iv.hex() + token):
            fake_iv = bytes([char]) + fake_iv
            break
    step_padding = bytes([step+1]) * (step+1)
    next_padding = bytes([step+2]) * (step+1)
    fake_iv = xor(fake_iv, step_padding, next_padding)

iv = xor(fake_iv, pad(b'test123_guest'), bytes([17]) * 16)
hack_iv = xor(iv, pad(b'test123_guest'), pad(b'user456_admin'))
verify(hack_iv.hex() + token)

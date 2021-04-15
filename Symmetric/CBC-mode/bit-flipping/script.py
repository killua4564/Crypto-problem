
usr1 = 'a' * 10
pwd1 = 'a' * 27

usr2 = 'a' * 6
pwd2 = 'a' * 45

token1 = chuck(login(usr1, pwd1))
token2 = chuck(login(usr2, pwd2))

B23 = b'61616161616161616161616161616161'
B23_ = b'a27663ac616161616161616161616161'

C11 = token1[0]
C12 = token1[1]
C22 = token2[1]
C23 = token2[2]
C22_ = xor(C22, B23, B23_)

verify(C11 + C12 + C22_ + C23, vc)

# msgpack's data len byte will change three length when >= 32
# msgpack.dumps({'usr': usr, 'pwd': pwd, 'vc': vc})
# ==> \x83\xa3usr + len(usr) + usr + \xa3pwd + len(pwd) + pwd + \xa2vc + \xda\x00( + vc
# ==> 5 + 1 + len(usr) + 4 + 1 + len(pwd) + 3 + 3(?) + 40

'''
(1) len(usr) = 10, len(pwd) = 27
B11: \x83\xa3usr\xaaaaaaaaaaaa
B12: \xa3pwd\xbbaaaaaaaaaaa
B13: aaaaaaaaaaaaaaaa
B14: \xa2vc\xda\x00( + vc .....

iv: fixed
C11 = E(B11 xor iv)
C12 = E(B12 xor C11)
C13 = E(B13 xor C12)

(2) len(usr) = 6, len(pwd) = 31
B21: \x83\xa3usr\xa6aaaaaa\xa3pwd
B22: \xbfaaaaaaaaaaaaaaa
B23: aaaaaaaaaaaaaaaa  (\xa2vc\xacaaaaaaaaaaaa)
B24: \xa2vc\xda\x00( + vc .....

C21 = E(B21 xor iv)
C22 = E(B22 xor C21)
C23 = E(B23 xor C22)

and we want C23 decrypt will be B23' = \xa2vc\xacaaaaaaaaaaaa
so compute C22' = C22 xor B23 xor B23'

payload = C11 + C12 + C22' + C23
decrypt = B11 + B12 + idk + B23'

decrypt:
\x83\xa3usr\xaaaaaaaaaaaa
\xa3pwd\xbbaaaaaaaaaaa
[idc * 16]
\xa2vc\xacaaaaaaaaaaaa

\x83\xa3usr\xaaaaaaaaaaaa\xa3pwd\xbbaaaaaaaaaaabbbbbbbbbbbbbbbb\xa2vc\xacaaaaaaaaaaaa

msgpack.loads(decrypt(payload))
==> {b'usr': b'aaaaaaaaaa', b'pwd': b'aaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaa', b'vc': b'aaaaaaaaaaaaaaa'}
'''
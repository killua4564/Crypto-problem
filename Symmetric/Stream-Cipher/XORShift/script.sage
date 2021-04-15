F = GF(2)

SHL = companion_matrix([F(0)] * 64 + [F(1)], format='left')
SHR = companion_matrix([F(0)] * 64 + [F(1)], format='right')

M = identity_matrix(F, 64)
M += M * SHL ** 13
M += M * SHR ** 7
M += M * SHL ** 17

W, A, B = M, [], []
for binary in list(state):
	if binary != '.':
		A.append(W.T[0])  # leak last bit
		B.append(Integer(binary))
	W *= M

A = Matrix(F, A).T
B = vector(F, B)

# X = A.solve_left(Y) ==> XA = Y
S = A.solve_left(B)               # type(S) = Vector_mod2_dense
print('origin:', ZZ(list(S), 2))  # type(ZZ) = rings of integer

S = S * M ** 200
print('state:', ZZ(list(S), 2))
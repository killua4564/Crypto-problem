from Crypto.Util.number import *
from secret import FLAG

if __name__ == '__main__':
    e = 0x10001
    p, q = getPrime(1024), getPrime(1024)
    n = p * q

    m = bytes_to_long(FLAG.encode())
    c = pow(m, e, n)

    print(f'p = {p}')
    print(f'q = {q}')
    print(f'c = {c}')

# p = 162337169038563309495807685167762121970003858796035665512656496629162067130652445334999298995295727401540367672774036899902844826933378999379202093961823277715633711681943041410404513360896889030217510136861003624183812140530880156645490440510311805693126411518975066288584358801452117938124283534129750509683
# q = 154969080505114673491990432829139003325401759293706506896990548066492251455063418468163080006604169677003561131638283866696566575519798195125967148101107466712359839168611621393721067175793244389827197233989856803439806620234279481451309375664001288009830750297916011865551411009170641584523107269345275979729
# c = 4762561323788161582500791215816694383714708461529551468122849498219936768388256720333367110224965468055779943549815121113527480711703345774582745557485456411014354999136033130268723778002160694416324551749555126655424004976841750175623576387186111995744272466683246481471960513548214753287488315777069141985110571795618075097187096594639068995887384178301083561639159331620544759381103903544430503068575818565416285816539517783412102496641523900485746095422476630936124836108099761237028318957446214811954943289334508142658027884460634214557680578414783481655680749641341078650806289169405283301004468744675390369088

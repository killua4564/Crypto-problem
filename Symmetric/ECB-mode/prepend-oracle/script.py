
arr = [enc('A' * (15 - i)) for i in range(16)]

flag = ''
for i in range(len(enc('')))[:2]:
    for j in range(16):
        target = arr[j][i]
        for char in string.printable:
            if target == enc('A' * (15 - j) + flag + char)[i]:
                flag += char
                break

print(flag)

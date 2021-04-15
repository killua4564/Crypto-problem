

result = ''
for _ in range(len(flag)):
    for char in string.printable:
        if flag.startswith(something(result + char)):
            result += char
            break
print(result)

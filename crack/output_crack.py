input = open("binary.out", "rb")

def bun(x):
    return (x >= ord('0') and x <= ord('9')) or (x >= ord('a') and x <= ord('z')) or (x >= ord('A') and x <= ord('Z'))

def alege(x):
    if bun(x^ord(' ')):
        return (x^ord(' '))
    if bun(x^ord('a')):
        return (x^ord('a'))
    if bun(x ^ ord('i')):
        return (x ^ ord('i'))
    return (x ^ ord('e'))

for key_len in range(10, 16):
    input.seek(0)
    index = 0
    frq = [{} for _ in range(0, key_len)]
    byte = input.read(1)
    while byte:
        if byte not in frq[index]:
            frq[index][byte] = 1
        else:
            frq[index][byte] += 1
        index += 1
        index %= key_len
        byte = input.read(1)

    lst = []
    for i in range(0, key_len):
        acm = [(x, frq[i][x]) for x in frq[i]]
        acm = sorted(acm, key=(lambda x:-x[1]))
        lst.append(alege(int.from_bytes(acm[0][0], 'little')))

    acm = ""
    for x in lst:
        acm += chr(x)

    print(f"key length: {key_len} ",acm)

input.close()

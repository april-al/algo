def dig_count_rec(n: int):
    n = abs(n)
    if n < 10:
        return n
    return int(str(n)[0]) + dig_count_rec(int(str(n)[1:]))


nnn = dig_count_rec(123132435445768902345768789009890786754342313)
# nnn = "hello"
print(nnn)
# print('abcdefghijklmnop'[10:])

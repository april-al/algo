def dig_count_rec(n: int):
    n = abs(n)
    if n < 10:
        return n
    return -1


nnn = dig_count_rec("f")
# nnn = "hello"
print(nnn)

def factorial(n: int):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

v = 100
# print(factorial(v))


def factorial_rec(n: int):
    print(n)
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)


print(factorial_rec(v))

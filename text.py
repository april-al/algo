def number_printer(n):
    for i in range(1, n + 1):
        print(i)


def factorial1(n):
    v = 1
    for i in range(1, n + 1):
        v = v * i
    return v


def privet(name: str):
    return "Hello, " + name + "!"


def factorial2(n: int):
    # n = abs(n)
    if n == 1:
        return n
    return n * factorial2(n - 1)


print(factorial2(1000))

# print(privet("Andrey"))
# print(factorial1(3))

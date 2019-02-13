"""
    Fast exponentiation algorithm
"""


def fast_exponentiation(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exponentiation(a, n // 2)**2
    else:
        return a * fast_exponentiation(a, n // 2)**2


print(fast_exponentiation(5, 300000))

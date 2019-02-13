"""
    normal naïve exponentiation
"""


def normal_exponentiation(a, n):
    exponentiated_a = a
    if n >= 2:
        for i in range(1, n):
            exponentiated_a *= a
        return exponentiated_a
    else:
        return a


print(normal_exponentiation(5, 300000))

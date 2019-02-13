"""
    naive fibonacci
"""


def bad_fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


print(bad_fibonacci(100))

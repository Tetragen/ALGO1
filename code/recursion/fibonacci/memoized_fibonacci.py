"""
    memoized fibonacci
"""

m = 200
intermediate_values = [None for i in range(1, m + 1)]


def memo_fibonacci(n):
    if intermediate_values[n] is None:
        if n == 1 or n == 2:
            intermediate_values[n] = 1
        else:
            intermediate_values[n] = memo_fibonacci(
                n//2) + memo_fibonacci(n//3)
    return intermediate_values[n]


"""
    Write your own test
"""
print(memo_fibonacci(25))

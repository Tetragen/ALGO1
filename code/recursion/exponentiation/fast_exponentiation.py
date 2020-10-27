"""
    Fast exponentiation algorithm
"""
from termcolor import colored


def fast_exponentiation(a, n):
    """
        EDIT THIS FUNCTION
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exponentiation(a, n-1)
    else:
        return a * fast_exponentiation(a, n-1)


def test_function(a, n):
    """Function to test recursive method
    by comparing with the factorial function
    from the math module

    :to_test: int

    """
    recursive = fast_exponentiation(a, n)
    math_function = pow(a, n)
    if recursive == math_function:
        print(
            colored(f"a={a}, n={n} result ok: {math_function}", "blue", attrs=["bold"]))
    else:
        print(colored(f"a={a}, n={n} wrong result: {math_function} vs " +
                      f"{recursive} (recursive)",
                      "yellow",
                      attrs=["bold"]))


test_function(13, 7)
test_function(5, 20)

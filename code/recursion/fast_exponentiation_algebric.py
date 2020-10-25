"""
    fast exponentiation without recursion
"""
from termcolor import colored


def fast_exponentiation_algebric(a, n):
    """
        compute a^n using the binary decomposition of n
    """

    # get the binary decomposition of n
    if n == 0:
        return 1
    else:
        binary_n = binary_decomposition(n)
        d = len(binary_n)

        # compute the powers a^(2^i) for i<=d
        powers_of_a = [a]
        for i in range(1, d):
            powers_of_a.append(powers_of_a[-1]**2)

        # we can write this also with list comprehensions
        # powers_of_a = [a**(2**i) for i in range(d)]

        # finally compute a^n
        result = 1
        for i in range(len(binary_n)):
            if binary_n[i] == 1:
                result *= powers_of_a[i]
        return result


def binary_decomposition(n):
    """
        decompose n in powers of 2
        please note that here, this corresponds to the
        REVERSED binary writing of n.
    """
    decomposition = list()
    if n == 0:
        return [0]
    else:
        temp = n
        while temp > 0:
            r = temp % 2
            decomposition.append(int(r))
            temp = (temp-r)/2
        return decomposition


"""
    test functions
"""


def test_binary_decomposition(n, decomposition):
    result = 0
    for i in range(len(decomposition)):
        if decomposition[i] == 1:
            result += 2**i
    if n == result:
        print(colored(f"binary decomposition is correct : ", "blue") +
              f"n={n} decomposition {decomposition}\n")
    else:
        print(colored("wrong binary decomposition : ", "red") +
              f"n={n} decomposition {decomposition}\n")


def test_method(a, n):
    print(f"testing method for a={a} and n={n}")
    function_result = fast_exponentiation_algebric(a, n)
    pow_result = pow(a,n)
    if function_result == pow_result:
        print(colored(f"result is correct : {pow_result}\n", "blue"))
    else:
        print(colored(f"wrong result !\n", "red") +
              f"pow gives {pow(a,n)}\n" +
              f"function gives {function_result}\n")


"""
    test our results
"""
test_binary_decomposition(5, binary_decomposition(5))
test_method(4, 5)
test_method(13, 5)

test_binary_decomposition(9, binary_decomposition(9))
test_method(4, 9)
test_method(13, 9)

test_binary_decomposition(2000, binary_decomposition(2000))
test_method(4, 2000)
test_method(13, 2000)

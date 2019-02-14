"""
    naive fibonacci
"""

import cProfile
import sys
import os


def bad_fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


pr = cProfile.Profile()
pr.enable()


# code to be profiled
print(bad_fibonacci(30))


pr.disable()
stats_file = open("{}.txt".format(os.path.basename(__file__)), 'w')
sys.stdout = stats_file
pr.print_stats(sort='time')

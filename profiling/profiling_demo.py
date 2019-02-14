import numpy as np
import os
import cProfile
import sys

pr = cProfile.Profile()
pr.enable()

# code to be profiled
a = 0
for step in range(20):
    x = step*2
    x = 2*3
    b = np.random.rand(10, 10)

pr.disable()
stats_file = open("{}.txt".format(os.path.basename(__file__)), 'w')
sys.stdout = stats_file
pr.print_stats(sort='time')

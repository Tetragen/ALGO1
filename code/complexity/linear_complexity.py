"""
    measure the complexity of a simple loop
"""

import matplotlib.pyplot as plt
import os
# import math
from time import time

min_size = 1
max_size = 10**7
step = int(max_size / 5)
sizes = range(min_size, max_size + 2, step)
# sizes = [10**i for i in range(0, 8)]


times = []

for size in sizes:
    print(str(size) + ' multiplications')
    t0 = time()
    for j in range(size):
        x = 2 * 3
    times.append(time() - t0)

# use the logarithm
# log_sizes = [math.log(size) for size in sizes]

title = 'Complexity of a sequence of multiplications'
filename = 'linear.pdf'
# plt.plot(log_sizes, times, 'o')
plt.plot(sizes, times, 'o')
plt.xlabel('number of multiplications')
plt.ylabel('computation time (seconds)')
plt.title(title)
if not os.path.exists("./images/"):
    os.mkdir("./images")
plt.savefig('images/' + filename)
plt.close()

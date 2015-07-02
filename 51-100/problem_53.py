__author__ = 'Yann'

import math


def selecting_combinatorics(r, n):
    if n < r:
        return 0

    return int(math.factorial(n) / math.factorial(r) / math.factorial(n - r))


limit = 1000000
lst = []

for n in range(1, 101):
    for r in range(1, n):
        if selecting_combinatorics(r, n) > limit:
            lst.append([r,n])


print(len(lst))

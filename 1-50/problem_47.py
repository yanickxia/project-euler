__author__ = 'Yann'

from utils.math_tools import *

primes = find_less_n_primes(1000)

#n = 134043
n = 646
couters = 4
while True:
    c = couters
    is_find = False
    while c > 0:
        if not is_dived_by_primes(n + (couters - c), primes, couters):
            n = n + (couters - c)
            break
        if c == 1:
            print(n)
            is_find = True
        c -= 1

    if is_find:
        break

    n += 1

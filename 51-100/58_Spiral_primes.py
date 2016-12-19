__author__ = 'Yann'

from utils.math_tools import *

import pyprimes

step_len, start_num = 2, 1

spiral_prime = []

primes_counter = 0
n_counter = 2

while True:
    crycle = 4
    while crycle:
        start_num += step_len
        crycle -= 1
        # spiral_prime.append(start_num)
        if pyprimes.isprime(start_num):
            primes_counter += 1

    n_counter += 2
    step_len += 2

    # per = per_primes(spiral_prime)
    per = primes_counter / (2.0 * n_counter)
    # print("side_length %s, primes %s, per %s" % (2 * n_counter, primes_counter, per))
    if per < 0.1:
        break

print(n_counter - 1)

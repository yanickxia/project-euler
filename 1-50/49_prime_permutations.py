__author__ = 'Yann'

import utils.math_tools as math_tools

primes = math_tools.find_less_n_primes(9999)


def is_permutations(x:int, y:int, primes:list):
    diff = y - x
    z = y + diff

    if z in primes:
        s_x = sorted(str(x))
        s_y = sorted(str(y))
        s_z = sorted(str(z))

        if s_x == s_y == s_z:
            return True


for i in range(len(primes) - 2):
    if primes[i] < 1000:
        continue

    for j in range(i + 1, len(primes) - 1):
        if is_permutations(primes[i], primes[j], primes):
            print(primes[i], primes[j], 2 * primes[j] - primes[i])

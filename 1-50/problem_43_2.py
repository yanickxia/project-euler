__author__ = 'Yann'

from utils.Primes import Primes
from utils.math_tools import *

primes = Primes().find_less_n_primes(18)


def is_divisible(n):
    n = str(n)
    gap = 3
    for i in range(1, len(n) - 2):
        sub_n = int(n[i:i + gap])
        if not is_integer(sub_n / primes[i - 1]):
            return False
    return True


numbers = gen_pandigital_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], '', [])

sum_number = 0
for i in numbers:

    i = str(i)

    if int(i[2:10]) not in [30952867, 60357289, 6357289]:
        continue

    if is_divisible(i):
        sum_number += int(i)

print(sum_number)
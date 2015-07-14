__author__ = 'Yann'

from utils.Primes import Primes
from utils.math_tools import *

primes = Primes().find_less_n_primes(18)

numbers = gen_pandigital_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], '', [])

for i in range(len(numbers)):

    n = str(numbers[i])
    if len(n) != 10:
        numbers.remove(n)

    if n[5] != '0' or n[5] != '5':
        numbers.remove(n)

    if int(n[3]) % 2 != 0:
        numbers.remove(n)


print(numbers)


def is_divisible(n):
    n = str(n)
    gap = 3
    for i in range(1, len(n) - 2):
        sub_n = int(n[i:i + gap])
        if not is_integer(sub_n / primes[i - 1]):
            return False
    return True


for number in numbers:
    if is_divisible(number):
        print(number)

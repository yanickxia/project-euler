__author__ = 'Yann'

from utils.Primes import Primes
import math
from utils.math_tools import *

primes_generntion = Primes()
primes = primes_generntion.find_less_n_primes(10000)

n = 3
while True:

    flag = False
    for x in primes:
        if x > n:
            break
        if is_integer(math.sqrt((n - x) / 2)):
            flag = True
    if flag == False:
        print('False :', n)
        break

    n += 2

# -*- coding:utf-8 -*-

import math
import utils.primes_tools as pt

PRIMES = set(pt.primes(100_000_000))


def is_prime_divisor(n):
    i = 1
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            d = i + int((n / i))
            if d not in PRIMES:
                return False

        i += 1

    return True


if __name__ == '__main__':

    print(is_prime_divisor(30))

    i, sum_i = 1, 0
    while i <= 100_000_000:
        if is_prime_divisor(i):
            sum_i += i
        i += 1

    print(sum_i)


# 太慢了好像也没有什么好办法
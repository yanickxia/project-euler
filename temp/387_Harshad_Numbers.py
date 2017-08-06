# -*- coding:utf-8 -*-

from utils import primes_tools as pt
from utils import math_tools as mt

primes_less_10000 = set(pt.primes(10000))


def is_harshad(a):
    return int(a) % sum_of_its_digits(a) == 0


def sum_of_its_digits(a):
    return sum(map(lambda x: int(x), str(a)))


def is_right_truncatable_harshad_number(a):
    a_str = str(a)

    if len(a_str) == 1:
        return True
    else:
        return int(a) % sum_of_its_digits(a) == 0 \
               and is_right_truncatable_harshad_number(int(a_str[:-1]))


def is_stroger_harshad_number(a):
    pass


##### 以上不太可能


BASE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PLUS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

strong_hs = []

if __name__ == '__main__':
    while BASE[0] < 10000:
        new_base = []
        for b in BASE:
            for p in PLUS:
                bp = int(str(b) + str(p))
                if mt.is_probable_prime(bp) \
                        and mt.is_probable_prime(int(b / sum_of_its_digits(b))) \
                        and is_harshad(b):
                    strong_hs.append(bp)
                if is_harshad(bp):
                    new_base.append(bp)
        BASE = new_base

    print(sum(strong_hs))

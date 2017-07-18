# -*- coding:utf-8 -*-

import math


def divisor_of_n(n):
    rs = [1, n]
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            rs.append(i)
            rs.append(int(n / i))
        i += 1
    return sorted(rs)

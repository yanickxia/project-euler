# -*- coding:utf-8 -*-

import math
from fractions import Fraction

# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# a0 -> 2, a1 -> 1, a2 -> 2
an_list = []


def next_a(fs, before):
    fs = 1 / (fs - before)
    return int(fs), fs


fs = math.e
a = int(fs)
# an_list.append(a)
fs_a = a
# get all an
# http://mathworld.wolfram.com/ContinuedFraction.html
for i in range(99):
    nextN = next_a(fs, a)
    fs = nextN[1]
    a = nextN[0]
    an_list.append(a)

print(an_list)

nm = an_list[0]

f_n = 0

y = Fraction(0)
for x in an_list[::-1]:
    y = Fraction(Fraction(1), y + x)

y += Fraction(fs_a)

# http://s0.wp.com/latex.php?zoom=2&latex=n_i+%3D+m_i+%2A+n_%7Bi-1%7D+%2B+n_%7Bi-2%7D%2C+where%5C%3An_0%3D1%5C%3Aand%5C%3An_1%3D2&bg=ffffff&fg=000&s=0

# 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1 这里是是  1,2,1  -> 1,4,1  -> 1,6,1 这规律


# Project Euler Problem 65
n0, n1, L = 1, 2, 100

for i in range(2, L + 1):
    n0, n1 = n1, n0 + n1 * (1 if i % 3 else 2 * i // 3)

print(sum(map(int, str(n1))))

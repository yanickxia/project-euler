# -*- coding:utf-8 -*-

import math

# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# a0 -> 2, a1 -> 1, a2 -> 2

an_list = []


def next_a(fs, before):
    fs = 1 / (fs - before)
    return int(fs), fs


fs = math.e
a = int(fs)
an_list.append(a)

# get all an
# http://mathworld.wolfram.com/ContinuedFraction.html
for i in range(10):
    nextN = next_a(fs, a)
    fs = nextN[1]
    a = nextN[0]
    an_list.append(a)

print(an_list)

nm = an_list[0]

f_n = 0

# 实现一个分数库

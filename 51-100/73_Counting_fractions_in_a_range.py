# -*- coding:utf-8 -*-
from fractions import Fraction

d = 12000

left_n = Fraction(1, 3)
right_n = Fraction(1, 2)

n_set = set()

for i_denominator in range(4, d + 1, 1):
    for i_numerator in range(int(i_denominator / 3), d + 1, 1):
        i = Fraction(i_numerator, i_denominator)
        if left_n < i < right_n:
            n_set.add(i)
        if i > right_n:
            break

print(len(n_set))
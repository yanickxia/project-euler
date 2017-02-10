# -*- coding:utf-8 -*-
from fractions import Fraction

d = 1000000
max_n = Fraction(3, 7)
start_n = Fraction(1, d)

close_n = 0


def m_n_fraction(m):
    x = m * max_n.numerator
    y = m * max_n.denominator

    new_f = Fraction(x - 1, y)
    while new_f.denominator > d:
        x -= 1
        new_f = Fraction(x, y)

    return new_f


for i in range(2, d + 1, 1):
    new_n = m_n_fraction(i)
    if new_n > close_n:
        close_n = new_n


print(close_n)
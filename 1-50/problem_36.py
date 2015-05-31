__author__ = 'Yann.Xia'

import math


def is_palindromes_decimal(num):
    n = num
    power = 0
    while num > 0:
        power *= 10
        power += num % 10
        num = int(num / 10)
    if power == n:
        return True
    return False

def is_palindromes_binary(num):
    n = num
    power = 0
    while num > 0:
        power *= 2
        power += num % 2
        num = int(num / 2)
    if power == n:
        return True
    return False

s = 0
for i in range(1, 1000000):
    if is_palindromes_decimal(i) and is_palindromes_binary(i):
        s += i

print(s)
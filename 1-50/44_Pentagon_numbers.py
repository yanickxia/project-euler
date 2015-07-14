__author__ = 'Yann'

import math


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def is_pentagonal(n):
    return str(get_x(3, -1, (-n) * 2)).split('.')[1] == '0'


def get_x(a, b, c):
    return (-b + abs(math.sqrt(math.pow(b, 2) - 4 * a * c))) / (2 * a)


notFound = True
result = 0
i = 1
while notFound:
    i += 1
    n = pentagonal(i)
    for j in range(1, i):
        m = pentagonal(j)
        if is_pentagonal(n - m) and is_pentagonal(n + m):
            result = n - m
            notFound = False
            break

print(result)